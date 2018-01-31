import os

from bson.json_util import dumps
from flask import request
from werkzeug.exceptions import InternalServerError

from dennett.trials.models import TrialsCollection
from . import trials


@trials.route('v1/trials', methods=['GET', 'POST'])
def trials_list_v1():
    collection = TrialsCollection(str(os.environ['DB_COLLECTION_V1']))

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
    collection = TrialsCollection(str(os.environ['DB_COLLECTION_V2']))

    if request.method == 'GET':
        filters = request.args.to_dict()
        the_trials = collection.fetch(filters)
        return dumps(the_trials)

    if request.method == 'POST':
        data = request.get_json()
        if isinstance(data, list):
            saved_trials_ids = collection.add_batch(data)
        else:
            saved_trials_ids = [collection.add(data)]
        if len(saved_trials_ids) == 0:
            raise InternalServerError
        return dumps(saved_trials_ids), 201
