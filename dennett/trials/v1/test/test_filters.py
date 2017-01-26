import requests
from database import mongo
from conftest import session, URL_PREFIX
from dennett.trials.v1.models import Trial


TRIALS = [
    {'id': '1', 'user': '0001', 'op_type': '3x1'},
    {'id': '2', 'user': '0002', 'op_type': '3x2'},
    {'id': '3', 'user': '0003', 'op_type': '3x3'},
    {'id': '4', 'user': '0001', 'op_type': '3x4'},
    {'id': '5', 'user': '0002', 'op_type': '3x5'},
    {'id': '6', 'user': '0001', 'op_type': '3x1'},
    {'id': '7', 'user': '0002', 'op_type': '4x2'},
    {'id': '8', 'user': '0003', 'op_type': '4x3'},
    {'id': '9', 'user': '0001', 'op_type': '4x4'},
    {'id': '10', 'user': '0002', 'op_type': '4x5'},
    {'id': '11', 'user': '0003', 'op_type': '4x6'},
    {'id': '12', 'user': '0003', 'op_type': '4x6'}
]



def test_page_0(session):
    page_size = 5
    for trial in TRIALS:
        requests.post(URL_PREFIX + 'v1/trials', json=trial)
    url = URL_PREFIX + 'v1/trials?page-size={}'.format(page_size)
    data = requests.get(url).json()
    stored_ids = set(trial['id'] for trial in data)
    original_ids = set(trial['id'] for trial in TRIALS[:page_size]) 
    assert stored_ids == original_ids


def test_page_1(session):
    page_size = 3
    page = 2
    for trial in TRIALS:
        requests.post(URL_PREFIX + 'v1/trials', json=trial)
    url = URL_PREFIX + 'v1/trials?page-size={}&page={}'.format(page_size, page)
    data = requests.get(url).json()
    stored_ids = set(trial['id'] for trial in data)
    original_ids = set(trial['id'] for trial in TRIALS[page*page_size:(page+1)*page_size]) 
    assert stored_ids == original_ids
