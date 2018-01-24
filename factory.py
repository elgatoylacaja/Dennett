from flask import Flask

from blueprints import register_blueprints
from config import Config
from database import mongo


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)
    register_blueprints(app)
    return app
