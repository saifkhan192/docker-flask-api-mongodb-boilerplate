import os
import sys

# Import the main Flask app
from flask_app import app, mongodb

# Get Blueprint Apps
from fontend_app import fontend_app
from auth_app import auth_app
from helper import start_debugger


# Register Blueprints
app.register_blueprint(fontend_app)
app.register_blueprint(auth_app)

if __name__ == "__main__":
    # locally PORT 5000, Heroku will assign its own port
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', False)
    if os.environ.get('VSCODE_DEBUG'):
        start_debugger()
        app.run(host='0.0.0.0', port=port, debug=False, use_evalex=False)
    else:
        app.run(host='0.0.0.0', port=port, debug=debug, use_evalex=False)
