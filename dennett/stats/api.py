import os
from dennett.trials.models import Trial
from bson.json_util import dumps
from . import stats


@stats.route('v1/stats', methods=['GET'])
def stats_detail_v1():
    DB_COLLECTION_V1 = str(os.environ['DB_COLLECTION_V1'])
    s = Trial.stats(DB_COLLECTION_V1)
    return dumps(s)


@stats.route('v2/stats', methods=['GET'])
def stats_detail_v2():
    DB_COLLECTION_V2 = str(os.environ['DB_COLLECTION_V2'])
    s = Trial.stats(DB_COLLECTION_V2)
    return dumps(s)
