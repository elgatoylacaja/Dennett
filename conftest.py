import pytest

from database import mongo
from dennett.personal_data.models import PersonalDataCollection
from dennett.trials.models import TrialsCollection
from factory import create_app


@pytest.fixture
def session():
    _app = create_app()
    with _app.app_context():
        drop_collections()
        yield
        drop_collections()


def drop_collections():
    mongo.db.drop_collection(TrialsCollection.V1_COLLECTION_NAME)
    mongo.db.drop_collection(TrialsCollection.V2_COLLECTION_NAME)
    mongo.db.drop_collection(PersonalDataCollection.V2_COLLECTION_NAME)


URL_PREFIX = 'http://localhost:5000/api/'
