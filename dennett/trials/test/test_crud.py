import requests
from conftest import session, URL_PREFIX


def test_post_trial(session):
    trial = {
        'user': '0001',
        'op_type': '3x2'
    }
    r = requests.post(URL_PREFIX + 'v1/trials', json=trial)
    assert r.status_code == 201


def test_get_empty_trials_list(session):
    r = requests.get(URL_PREFIX + 'v1/trials')
    data = r.json()
    assert r.status_code == 200
    assert len(data) == 0


def test_get_trials_list(session):
    trials = [
        {'user': '0001', 'op_type': '3x1'},
        {'user': '0002', 'op_type': '3x2'},
        {'user': '0003', 'op_type': '3x3'}
    ]
    for trial in trials: 
        requests.post(URL_PREFIX + 'v1/trials', json=trial)
    data = requests.get(URL_PREFIX + 'v1/trials').json()
    assert len(data) == 3


def test_get_trial(session):
    trial = {
        'user': '0001',
        'op_type': '3x2'
    }
    data = requests.post(URL_PREFIX + 'v1/trials', json=trial).json()
    r = requests.get(URL_PREFIX + 'v1/trials/' + data['$oid'])
    assert r.status_code == 200


def test_get_unexisting_trial(session):
    r = requests.get(URL_PREFIX + 'v1/trials/012345678901234567891234')
    assert r.status_code == 404
