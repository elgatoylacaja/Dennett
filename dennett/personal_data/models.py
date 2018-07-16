import os

from dennett.models import MongoCollection


class PersonalDataCollection(MongoCollection):
    V2_COLLECTION_NAME = '%s_v2_personal_data' % str(os.environ['ENVIRONMENT'])
