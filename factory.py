from flask import Flask
from database import db

from app.trials.api import trials


def register_blueprints(app):
    BLUEPRINTS = [trials]
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint, url_prefix='/api/v1')


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)
    register_blueprints(app)
    return app
