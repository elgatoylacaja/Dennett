from flask import request
from models import Trial
from flask import Blueprint
from werkzeug.exceptions import HTTPException
import tasks



trials = Blueprint('trials_v1', __name__)



@trials.route('v1/trials', methods=['GET', 'POST'])
def trials_list():

    if request.method == 'GET':
        try:
            return Trial.get_all()
        except HTTPException as e:
            return e

    if request.method == 'POST':
        data = request.get_json()
        try:
            id = Trial.post(data)
            return id, 201
        except HTTPException as e:
            return e


@trials.route('v1/trials/<id>', methods=['GET', 'DELETE'])
def trials_detail(id):

    if request.method == 'GET':
        try:
            trial = Trial.get(id)
            return trial
        except HTTPException as e:
            return e

    if request.method == 'DELETE':
        try:
            Trial.delete(id)
            return id, 204 
        except HTTPException as e:
            return e



@trials.route('v1/backup', methods=['GET'])
def trials_backup():
    file_resource = tasks.backup()
    if file_resource:
        return 'Success', 200
    return 'Unable to create backup', 500
