import os

import pytest

from database import mongo
from factory import create_app


@pytest.fixture
def session():
    _app = create_app()
    with _app.app_context():
        mongo.db.drop_collection(str(os.environ['DB_COLLECTION_V1']))
        yield
        mongo.db.drop_collection(str(os.environ['DB_COLLECTION_V1']))


URL_PREFIX = 'http://localhost:5000/api/'
