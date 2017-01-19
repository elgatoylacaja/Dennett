import pytest
from app import create_app
from database import db, mongo


@pytest.fixture(scope='session')
def app():
    _app = create_app()
    with _app.app_context():
        yield _app
 

@pytest.fixture(scope='function')
def session(app):
    db.create_all()
    yield 
    db.drop_all()
    mongo.db.drop_collection('trials')


URL_PREFIX = 'http://localhost:8000/api/'
