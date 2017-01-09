import sys
from flask import Flask
from database import db


def register_blueprints(app):
    BLUEPRINTS = []
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint, url_prefix='/api/v1')


def configure(app):
    if sys.argv[1] == 'develop':
        app.config.from_object('config.DevelopmentConfig')
    if sys.argv[1] == 'test':
        app.config.from_object('config.TestingConfig')


if __name__ == '__main__':
    app = Flask(__name__)
    register_blueprints(app)
    configure(app)
    db.init_app(app)
    app.run(threaded=True)
