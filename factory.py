from flask import Flask
from database import db, mongo

from app.trials.api import trials_blueprint


def register_blueprints(app):
    BLUEPRINTS = [trials_blueprint]
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint, url_prefix='/api/')


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)
    mongo.init_app(app)
    register_blueprints(app)
    return app
