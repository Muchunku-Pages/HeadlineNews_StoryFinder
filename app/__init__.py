from ensurepip import bootstrap
from .main import main as main_blueprint
from .requests import configure_request
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


def create_app(config_name):

    app = Flask(__name__)

# Generate the app configurations
    app.config.from_object(config_options[config_name])

   
# Register Blueprint

    app.register_blueprint(main_blueprint)

# Set config

    configure_request(app)

 # To add views and forms

    return app
       