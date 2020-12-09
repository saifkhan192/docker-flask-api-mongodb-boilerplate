# from myapp import create_app
import os, sys, pytest
from flask import Flask
sys.path.append('/app/application')

def create_app():
   # create app
   app = Flask("flask_test", root_path=os.path.dirname(__file__))
   app.config["MONGODB_SETTINGS"] = {
      "host": os.environ.get('MONGO_URI'),
      "db": os.environ.get('MONGO_DATABASE')
   }
   from fontend_app import fontend_app
   from auth_app import auth_app
   app.register_blueprint(fontend_app)
   app.register_blueprint(auth_app)
#    app.config.from_pyfile('./config.py)
   return app

@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()
    return client