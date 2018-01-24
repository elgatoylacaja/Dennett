import os

from bson.json_util import dumps

from dennett.trials.models import TrialsCollection
from . import stats


@stats.route('v1/stats', methods=['GET'])
def stats_detail_v1():
    return stats_detail(str(os.environ['DB_COLLECTION_V1']))


@stats.route('v2/stats', methods=['GET'])
def stats_detail_v2():
    return stats_detail(str(os.environ['DB_COLLECTION_V2']))


def stats_detail(db_collection_name):
    collection = TrialsCollection(db_collection_name)
    s = collection.stats()
    return dumps(s)
