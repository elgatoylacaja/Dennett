import requests
from database import mongo
from conftest import session, URL_PREFIX
from dennett.trials.v1.models import Trial
from dennett.trials.v1.tasks import send_mail


TRIALS = [
    {'order': '1', 'user': '0001', 'op_type': '3x1'},
    {'order': '2', 'user': '0002', 'op_type': '3x2'},
    {'order': '3', 'user': '0003', 'op_type': '3x3'},
    {'order': '4', 'user': '0001', 'op_type': '3x4'},
    {'order': '5', 'user': '0002', 'op_type': '3x5'},
    {'order': '6', 'user': '0001', 'op_type': '3x1'},
    {'order': '7', 'user': '0002', 'op_type': '4x2'},
    {'order': '8', 'user': '0003', 'op_type': '4x3'},
    {'order': '9', 'user': '0001', 'op_type': '4x4'},
    {'order': '10', 'user': '0002', 'op_type': '4x5'},
    {'order': '11', 'user': '0003', 'op_type': '4x6'},
    {'order': '12', 'user': '0003', 'op_type': '4x6'}
]


def test_backup(session):

    for trial in TRIALS: 
        requests.post(URL_PREFIX + 'v1/trials', json=trial)
    data = requests.get(URL_PREFIX + 'v1/trials').json()
    assert len(data) == 12

    Trial.export_to('5_oldest', 5)
    mongo.db.drop_collection('trials')
    data = requests.get(URL_PREFIX + 'v1/trials').json()
    assert len(data) == 0

    Trial.import_from('5_oldest')
    data = requests.get(URL_PREFIX + 'v1/trials').json()
    assert len(data) == 5
