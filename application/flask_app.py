import sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # set /app/application as working dir
from flask import Flask, render_template, request, redirect, abort
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from models.admin_models import *
import flask_debugtoolbar

app = Flask('Flask App')

Base = declarative_base()

app.debug = True if os.environ.get('flask_debug') else False
app.config['SECRET_KEY'] = os.environ.get('FLASK_APP_SECRET_KEY', os.urandom(32) )
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config["MONGODB_SETTINGS"] = {
   "host": os.environ.get('MONGO_URI'),
   "db": os.environ.get('MONGO_DATABASE')
}
# print(app.config["MONGODB_SETTINGS"] )
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = bool(os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS'))
app.config["SQLALCHEMY_ECHO"] = bool(os.environ.get('SQLALCHEMY_ECHO'))

# set second db config
app.config['SQLALCHEMY_BINDS'] = {
   'db2': os.environ.get('SQLALCHEMY_DATABASE_URI_DB2')
}

mongodb = MongoEngine(app) # connect MongoEngine with Flask App
app.session_interface = MongoEngineSessionInterface(mongodb) # sessions w/ mongoengine

db = SQLAlchemy()
db.init_app(app)


# Flask BCrypt will be used to salt the user password
flask_bcrypt = Bcrypt(app)
app.flask_bcrypt = flask_bcrypt

# Associate Flask-Login manager with current app
login_manager = LoginManager()
login_manager.init_app(app)

# optional debugging stuff
# app.config['DEBUG_TB_PANELS'] = [
#    'flask_debugtoolbar.panels.versions.VersionDebugPanel',
#    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
#    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
#    'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
#    'flask_debugtoolbar.panels.template.TemplateDebugPanel',
#    'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
#    'flask_debugtoolbar.panels.logger.LoggingPanel',
#    'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
#    # Add the MongoDB panel
#    # 'flask_debugtoolbar_mongo.panel.MongoDebugPanel',
# ]
# app.config['DEBUG_TB_MONGO'] = {
#   'SHOW_STACKTRACES': True,
#   'HIDE_FLASK_FROM_STACKTRACES': True
# }

# app.config['DEBUG_TB_PROFILER_ENABLED'] = True
# app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

if app.debug:
   toolbar = flask_debugtoolbar.DebugToolbarExtension(app)

getAdminViews(app,mongodb.get_db())