from dennett.admin.views import admin
from dennett.stats.api import stats
from dennett.trials.api import trials


def register_blueprints(app):
    app.register_blueprint(trials, url_prefix='/api/')
    app.register_blueprint(stats, url_prefix='/api/')
    app.register_blueprint(admin, url_prefix='/')
