from bson.json_util import dumps
from flask import request
from werkzeug.exceptions import InternalServerError

from dennett.api import simple_endpoint
from dennett.trials.models import TrialsCollection
from . import trials


@trials.route('v1/trials', methods=['GET', 'POST'])
def trials_list_v1():
    collection = TrialsCollection(TrialsCollection.V1_COLLECTION_NAME)

    if request.method == 'GET':
        filters = request.args.to_dict()
        the_trials = collection.fetch(filters)
        return dumps(the_trials)

    if request.method == 'POST':
        data = request.get_json()
        the_id = collection.add(data)
        if not the_id:
            raise InternalServerError
        return dumps(the_id), 201


@trials.route('v2/trials', methods=['GET', 'POST'])
def trials_list_v2():
    collection = TrialsCollection(TrialsCollection.V2_COLLECTION_NAME)
    return simple_endpoint(collection)
