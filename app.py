import os
from flask import Flask
from database import db, mongo
from dennett.trials.v1.api import trials as trials_v1
from dennett.trials.v2.api import trials as trials_v2


def register_blueprints(app):
    app.register_blueprint(trials_v1, url_prefix='/api/')
    app.register_blueprint(trials_v2, url_prefix='/api/')


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('DENNETT_CONFIG')
    db.init_app(app)
    mongo.init_app(app)
    register_blueprints(app)
    return app


app = create_app()
