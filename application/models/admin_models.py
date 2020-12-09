
from wtforms import form, fields
from flask_admin.contrib.pymongo import ModelView
from flask_admin.menu import MenuLink
from flask import current_app, redirect, url_for, abort
from flask_login import current_user
from flask_admin import Admin
import datetime


class LoginMenuLink(MenuLink):
    def is_accessible(self):
        return not current_user.is_authenticated


class LogoutMenuLink(MenuLink):
    def is_accessible(self):
        return current_user.is_authenticated


class MyModelView(ModelView):
    def is_accessible(self):
        # return not current_user.is_anonymous and current_user.has_role('super_admin')
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            msg = "Access denied"
            abort(403, msg)

    def _handle_view(self, name):
        if not self.is_accessible():
            return redirect('/login')

class AuthUserForm(form.Form):
    name = fields.TextField('name')
    email = fields.TextField('email')
    active = fields.BooleanField('active',default=True)
    isAdmin = fields.BooleanField('Is Admin',default=False)
    password = fields.PasswordField('Password')
    old_password = fields.HiddenField('Old password')
    timestamp = fields.DateTimeField('Timestamp')
    roles = fields.SelectMultipleField('roles',
        choices = [ ('super_admin', 'super_admin'),('admin', 'admin'), ]
    )
    permissions = fields.SelectMultipleField('permissions',
        choices = [ 
            ('create_account', 'create_account'),
            ('delete_account', 'delete_account'), 
            ('approve_post', 'approve_post'), 
        ]
    )

class AuthAccountView(MyModelView):
    column_list = ('name', 'email', 'active', 'isAdmin')
    column_sortable_list = ('name', 'email', 'active')
    form = AuthUserForm
    edit_modal = True
    create_modal = True
    can_delete = True
    details_modal = True
    column_searchable_list = ('name', 'email')

    def _on_model_change(self, form, model, is_created):
        if model.get('password'):
            ps_hash = current_app.flask_bcrypt.generate_password_hash(model['password'])
            model['password'] = ps_hash
        else:
            model['password'] = model.get('old_password')
    def on_form_prefill(self, form, id):
        form.old_password.data = form.password.data
        form.password.data = ""


class SubscriberForm(form.Form):
    name = fields.TextField('Name')
    email = fields.TextField('Email')
    created_at = fields.DateTimeField('Created at', default=datetime.datetime.now(), format="%Y-%m-%dT%H:%M:%S")

class SubscriberView(MyModelView):
    column_list = ('name', 'email', 'created_at')
    column_sortable_list = ('name', 'email', 'created_at')
    form = SubscriberForm
    edit_modal = True
    create_modal = True
    can_delete = True
    details_modal = True
    column_searchable_list = ('name', 'email')


def getAdminViews(app, mongo):
    admin = Admin(app, name="Admin Section", template_mode='bootstrap3')
    admin.add_link(MenuLink(name='Website', url="/", category=''))

    authUsersView = AuthAccountView(mongo["auth_users"] , 'Users')
    admin.add_view(authUsersView)

    subscribersView = SubscriberView(mongo["subscribers"] , 'Subscribers')
    admin.add_view(subscribersView)

    admin.add_link(LogoutMenuLink(name='Logout', url="/logout", category=''))