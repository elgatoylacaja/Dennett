from flask import request
from models import Trial
from flask import Blueprint



trials_blueprint = Blueprint('trials_blueprint', __name__)



@trials_blueprint.route('v1/trials', methods=['GET', 'POST'])
def v1_trials_list():

    if request.method == 'GET':
        return Trial.get_mongolab()

    if request.method == 'POST':
        data = request.get_json()
        trial = Trial.post_mongolab(data)
        return trial, 201


@trials_blueprint.route('v2/trials', methods=['GET', 'POST'])
def v2_trials_list():

    if request.method == 'GET':
        request_filters = request.args.to_dict()
        return Trial.get(request_filters)

    if request.method == 'POST':
        data = request.get_json()
        trial = Trial(data)
        t = trial.save()
        return t, 201
