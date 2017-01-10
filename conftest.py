import pytest
from factory import create_app
from database import db


@pytest.fixture(scope='session')
def app():
    yield create_app('config.TestingConfig')
 

@pytest.fixture(scope='function')
def session(app):
    ctx = app.app_context()
    ctx.push()
    db.session.begin_nested()
    yield 
    db.session.rollback()
    ctx.pop()


URL_PREFIX = 'http://localhost:5000/api/v1/'
