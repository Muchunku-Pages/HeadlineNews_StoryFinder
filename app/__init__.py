from flask import Flask
from config import config_options


def create_app(config_name):

    app = Flask(__name__)

    # Generate the app configurations
    app.config.from_object(config_options[config_name])

   
# Register Blueprint
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

# Set config
    from .request import configure_request
    configure_request(app)

 # To add views and forms

    return app
       