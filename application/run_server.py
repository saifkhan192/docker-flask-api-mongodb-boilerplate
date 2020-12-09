import os
import sys

# Import the main Flask app
from flask_app import app, mongodb

# Get Blueprint Apps
from fontend_app import fontend_app
from auth_app import auth_app

# Register Blueprints
app.register_blueprint(fontend_app)
app.register_blueprint(auth_app)

if __name__ == "__main__":
    # locally PORT 5000, Heroku will assign its own port
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', False)
    if os.environ.get('VSCODE_DEBUG'):
        import ptvsd
        debugAddress = os.environ.get(
            'DEBUG_CONFIG', "0.0.0.0:5678").split(":")
        print("debugAddress:", debugAddress)
        try:
            ptvsd.enable_attach(address=debugAddress)
        except Exception as ex:
            pass

        # breakpoint()
        # ptvsd.wait_for_attach()
        # print("local-app: http://localhost:",port)
        app.run(host='0.0.0.0', port=port, debug=debug, use_evalex=False)
    else:
        app.run(host='0.0.0.0', port=port, debug=debug, use_evalex=False)
