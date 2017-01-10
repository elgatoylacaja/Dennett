from flask import request
from flask import Blueprint
from models import Trial


trials = Blueprint('trials', __name__)


@trials.route('/trials', methods=['GET', 'POST'])
def trials_list():

    if request.method == 'GET':
        request_filters = request.args.to_dict()
        return Trial.get(request_filters)

    if request.method == 'POST':
        data = request.get_json()
        trial = Trial(data)
        t = trial.save()
        return t, 201
