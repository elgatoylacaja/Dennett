import os
from flask import request
from . import trials
from models import Trial
from bson.json_util import dumps
from werkzeug.exceptions import InternalServerError



@trials.route('v1/trials', methods=['GET', 'POST'])
def trials_list_v1():

    DB_COLLECTION_V1 = str(os.environ['DB_COLLECTION_V1'])

    if request.method == 'GET':
        filters = request.args.to_dict()
        trials = Trial.get(DB_COLLECTION_V1, filters)
        return dumps(trials)

    if request.method == 'POST':
        data = request.get_json()
        id = Trial.post(DB_COLLECTION_V1, data)
        if not id:
            raise InternalServerError
        return dumps(id), 201




@trials.route('v2/trials', methods=['GET', 'POST'])
def trials_list_v2():

    DB_COLLECTION_V2 = str(os.environ['DB_COLLECTION_V2'])

    if request.method == 'GET':
        filters = request.args.to_dict()
        trials = Trial.get(DB_COLLECTION_V2, filters)
        return dumps(trials)

    if request.method == 'POST':
        data = request.get_json()
        id = Trial.post(DB_COLLECTION_V2, data)
        if not id:
            raise InternalServerError
        return dumps(id), 201
