from flask import request
from flask import Blueprint


trials = Blueprint('trials', __name__)


@trials.route('/trials', methods=['GET', 'POST'])
def trials_list():

    if request.method == 'GET':
        return ''
