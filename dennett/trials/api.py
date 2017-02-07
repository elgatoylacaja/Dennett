from flask import request
from models import Trial
from werkzeug.exceptions import InternalServerError, NotFound
from bson.json_util import dumps
from . import trials



@trials.route('v1/trials', methods=['GET', 'POST'])
def trials_list():

    if request.method == 'GET':
        filters = request.args.to_dict()
        trials = Trial.get_many(filters)
        return dumps(trials)

    if request.method == 'POST':
        data = request.get_json()
        id = Trial.post(data)
        if not id:
            raise InternalServerError
        return dumps(id), 201



@trials.route('v1/trials/<id>', methods=['GET'])
def trials_detail(id):

    if request.method == 'GET':
        trial = Trial.get(id)
        if not trial:
            raise NotFound
        return dumps(trial)
