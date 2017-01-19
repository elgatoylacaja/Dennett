from dennett.trials.v1.api import trials as trials_v1
from dennett.trials.v2.api import trials as trials_v2


def register_blueprints(app):
    app.register_blueprint(trials_v1, url_prefix='/api/')
    app.register_blueprint(trials_v2, url_prefix='/api/')
