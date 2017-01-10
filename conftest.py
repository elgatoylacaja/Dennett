import pytest
from factory import create_app
from database import db


@pytest.fixture(scope='session')
def app():
    _app = create_app('config.TestingConfig')
    with _app.app_context():
        yield _app
 

@pytest.fixture(scope='function')
def session(app):
    db.create_all()
    yield 
    db.drop_all()


URL_PREFIX = 'http://localhost:5000/'
