from flask import Flask
from database import db, mongo

from app.trials.v1.api import trials as trials_v1
from app.trials.v2.api import trials as trials_v2


def register_blueprints(app):
    BLUEPRINTS = [trials_v1, trials_v2]
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint, url_prefix='/api/')


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)
    mongo.init_app(app)
    register_blueprints(app)
    return app
