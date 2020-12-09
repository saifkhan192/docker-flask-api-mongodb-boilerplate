from flask_app import app, mongodb, db
from models.auth import AuthUser
# from models.models import User, Post
from models.sqlacodegen_models import *


def run_seeders():
    # user = AuthUser(
    #     email="saifkhan912@gmail.com",
    #     active=True,
    #     roles=["super_admin"],
    #     permissions=["test_permission"]
    # )
    # user.set_password("1234")
    # try:
    #     with app.app_context():
    #         db.session.add(new_user)
    #         db.session.commit()
    # except Exception as identifier:
    #     pass


run_seeders()
