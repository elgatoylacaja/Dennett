from flask import Flask
from config import Config
from database import db, mongo
from blueprints import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    mongo.init_app(app)
    register_blueprints(app)
    return app
