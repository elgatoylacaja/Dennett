from dennett.trials.v1.models import Trial
from bson.json_util import dumps
from . import stats


@stats.route('v1/stats', methods=['GET'])
def stats_detail():
    s = Trial.stats()
    return dumps(s)
