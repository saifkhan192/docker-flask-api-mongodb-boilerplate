import os
import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (current_user, UserMixin, AnonymousUserMixin)
from flask_app import mongodb, abort, flask_bcrypt


class UserModel(mongodb.Document, UserMixin):
    email = mongodb.EmailField(unique=True)
    name = mongodb.StringField(default="Anonymous")
    password = mongodb.StringField(default=True)
    active = mongodb.BooleanField(default=True)
    isAdmin = mongodb.BooleanField(default=False)
    timestamp = mongodb.DateTimeField(default=datetime.datetime.now())
    roles = mongodb.ListField(mongodb.StringField())
    permissions = mongodb.ListField(mongodb.StringField())
    meta = {'collection': 'auth_users', 'strict': False}

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "email": self.email,
                "active": self.active,
                "isAdmin": self.isAdmin
                }


class ExtendedUserMixin():
    def has_role(self, needed_role):
        return needed_role and hasattr(self, 'roles') and needed_role in self.roles


class AuthUser(UserMixin, ExtendedUserMixin):
    def __init__(self, email=None, name=None, password=None, active=True, roles=[], permissions=[]):
        self.email = email
        self.password = password
        self.name = name
        self.active = active
        self.isAdmin = False
        self.id = None
        self.roles = roles
        self.permissions = permissions
        self._doc = None

    def save(self):
        newUser = UserModel(
            name=self.name,
            email=self.email,
            password=self.password,
            active=self.active
        )
        newUser.save()
        self.id = newUser.id
        return self

    def saveDoc(self, **params):
        doc = UserModel.objects.with_id(self.id)
        doc.setAtrributes(**params)
        doc.save()
        return self

    def setUserData(self, dbUser):
        if dbUser:
            self.email = dbUser.email
            self.password = dbUser.password
            self.active = dbUser.active
            self.isAdmin = dbUser.isAdmin
            self.id = dbUser.id
            self.roles = dbUser.roles
            self.permissions = dbUser.permissions
            return self
        else:
            return None

    def find(**args):
        result = list(UserModel.objects.filter(**args))
        return result

    def get_by_email(self, email):
        dbUser = UserModel.objects.get(email=email)
        return self.setUserData(dbUser)

    def get_by_email_w_password(self, email):
        try:
            return self.get_by_email(email)
        except Exception as ex:
            print("there was an error in get_by_email_w_password(): %s" % ex)
            return None

    def get_mongo_doc(self):
        if self.id:
            return self.get_by_id(self.id)
        else:
            return None

    def get_by_id(self, id_val):
        dbUser = UserModel.objects.with_id(id_val)
        return self.setUserData(dbUser)

    def match_password(self, password):
        try:
            return flask_bcrypt.check_password_hash(self.password, password)
        except ValueError as identifier:
            pass

        return False

    def set_password(self, password):
        ps_hash = flask_bcrypt.generate_password_hash(password)
        self.password = ps_hash


class Anonymous(ExtendedUserMixin, AnonymousUserMixin):
    name = u"Anonymous"


def permission_required(needed_role, needed_permissions=[]):
    """
    Check if a user has permission to a resource.
    [('user', 'read'), ('admin', 'create')]
    :return: a function or raise 403
    """
    def wrapper(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            if hasattr(current_user, 'roles') and 'super_admin' in current_user.roles:
                print("User is super_admin, allow ")
                return func(*args, **kwargs)

            if needed_role:
                if hasattr(current_user, 'roles') and needed_role in current_user.roles:
                    print("User has the role %s, allow " % needed_role)
                    return func(*args, **kwargs)
                else:
                    msg = 'You dont have [%s] role.' % needed_role
                    abort(403, msg)

            if needed_permissions and hasattr(current_user, 'permissions'):
                for each_perm in needed_permissions:
                    if each_perm in current_user.permissions:
                        print("User has the permission %s, allow " % each_perm)
                        return func(*args, **kwargs)
            abort(403, 'You dont have %s permission.' % needed_permissions)
        return wrapped
    return wrapper


def role_required(needed_role):
    """
    Check if a user has the role.
    :return: a function or raise 403
    """
    def wrapper(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            if needed_role and hasattr(current_user, 'roles') and needed_role in current_user.roles:
                return func(*args, **kwargs)
            msg = 'You dont have %s role.' % needed_role
            abort(403, msg)
        return wrapped
    return wrapper
