from flask import Flask
from config import Config
from database import mongo
from blueprints import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)
    register_blueprints(app)
    return app
