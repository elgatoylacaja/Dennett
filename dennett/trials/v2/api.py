from flask import request
from models import Trial
from . import trials


@trials.route('v2/trials', methods=['GET', 'POST'])
def trials_list():

    if request.method == 'GET':
        request_filters = request.args.to_dict()
        return Trial.get(request_filters)

    if request.method == 'POST':
        data = request.get_json()
        trial = Trial(data)
        t = trial.save()
        return t, 201
