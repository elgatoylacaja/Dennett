import pytest
from factory import create_app
from database import mongo
import os, re


def remove_test_backup_files():
    for f in os.listdir('.'):
        if re.search('backup*', f):
            os.remove(os.path.join('.', f))


@pytest.fixture(scope='session')
def app():
    _app = create_app()
    with _app.app_context():
        yield _app
 

@pytest.fixture(scope='function')
def session(app):
    mongo.db.drop_collection('test_v1')
    remove_test_backup_files()
    yield 
    mongo.db.drop_collection('test_v1')
    remove_test_backup_files()


URL_PREFIX = 'http://localhost:5000/api/'
