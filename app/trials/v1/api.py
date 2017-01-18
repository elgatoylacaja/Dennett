from flask import request
from models import Trial
from flask import Blueprint



trials = Blueprint('trials_v1', __name__)



@trials.route('v1/trials', methods=['GET', 'POST'])
def trials_list():

    if request.method == 'GET':
        return Trial.get_all()

    if request.method == 'POST':
        data = request.get_json()
        trial = Trial.post(data)
        return trial, 201



@trials.route('v1/trials/<id>', methods=['GET', 'DELETE'])
def trials_detail(id):

    if request.method == 'GET':
        trial = Trial.get(id)
        if trial:
            return trial
        return '', 404

    if request.method == 'DELETE':
        Trial.delete(id)
        return id, 204 
