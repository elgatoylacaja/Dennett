import requests
from conftest import session, URL_PREFIX


def test_get_empty_trials_list(session):
    r = requests.get(URL_PREFIX + 'v2/trials')
    data = r.json()
    assert r.status_code == 200
    assert len(data['data']) == 0


def test_post_trial(session):
    trial = {
        'user': '0001',
        'op_type': '3x2'
    }
    r = requests.post(URL_PREFIX + 'v2/trials', json=trial)
    assert r.status_code == 201
    assert trial == r.json()


def test_post_and_get_trials_list(session):
    trials = [
        {'user': '0001', 'op_type': '3x1'},
        {'user': '0002', 'op_type': '3x2'},
        {'user': '0003', 'op_type': '3x3'}
    ]
    for trial in trials: 
        requests.post(URL_PREFIX + 'v2/trials', json=trial)
    data = requests.get(URL_PREFIX + 'v2/trials').json()
    assert len(data['data']) == 3
    for trial in trials:
        assert trial in data['data']
