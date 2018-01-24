import os

from bson.json_util import dumps
from flask import request
from werkzeug.exceptions import InternalServerError

from dennett.trials.models import TrialsCollection
from . import trials


@trials.route('v1/trials', methods=['GET', 'POST'])
def trials_list_v1():
    return trials_list(db_collection_name=str(os.environ['DB_COLLECTION_V1']))


@trials.route('v2/trials', methods=['GET', 'POST'])
def trials_list_v2():
    return trials_list(db_collection_name=str(os.environ['DB_COLLECTION_V2']))


def trials_list(db_collection_name):
    collection = TrialsCollection(db_collection_name)

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
