import os

from dennett.models import MongoCollection


class TrialsCollection(MongoCollection):
    V1_COLLECTION_NAME = str(os.environ['DB_COLLECTION_V1'])
    V2_COLLECTION_NAME = '%s_v2_trials' % str(os.environ['ENVIRONMENT'])
