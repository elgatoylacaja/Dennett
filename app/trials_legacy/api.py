from flask import request
from flask import Blueprint
from app.trials.models import Trial
from translate_to_v2 import translate_to_v2


trials_legacy = Blueprint('trials_legacy', __name__)


@trials_legacy.route('/trials', methods=['POST'])
def trials_legacy_list():

    data_v1 = request.get_json()
    data_v2 = translate_to_v2(data_v1)
    trial = Trial(data_v2)
    t = trial.save()
    return t, 201
