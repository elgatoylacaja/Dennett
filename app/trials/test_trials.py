import requests
from conftest import session, URL_PREFIX


def test_get_empty_trials_list(session):
    r = requests.get(URL_PREFIX + 'v2/trials')
    assert r.status_code == 200
    data = r.json()
    assert len(data['data']) == 0


def test_post_trial(session):
    trial = {
        'user': '0001',
        'op_type': '3x2'
    }
    r = requests.post(URL_PREFIX + 'v2/trials', json=trial)
    assert r.status_code == 201
    data = r.json()
    assert data['user'] == trial['user']
    assert data['op_type'] == trial['op_type']


def test_post_and_get_trials_list(session):
    trial_1 = {
        'user': '0001',
        'op_type': '3x1'
    }
    trial_2 = {
        'user': '0002',
        'op_type': '3x2'
    }
    trial_3 = {
        'user': '0003',
        'op_type': '3x3'
    }
    trials = [trial_1, trial_2, trial_3]
    for index, trial in enumerate(trials):
        requests.post(URL_PREFIX + 'v2/trials', json=trial)
        r = requests.get(URL_PREFIX + 'v2/trials')
        data = r.json()
        assert len(data['data']) == index + 1

def test_filter_by_op_type(session):
    trial_1 = {
        'user': '0001',
        'op_type': '3x1'
    }
    trial_2 = {
        'user': '0002',
        'op_type': '3x1'
    }
    trial_3 = {
        'user': '0003',
        'op_type': '3x3'
    }
    trials = [trial_1, trial_2, trial_3]
    for trial in trials:
        requests.post(URL_PREFIX + 'v2/trials', json=trial)
    r = requests.get(URL_PREFIX + 'v2/trials?op_type=3x1')
    data = r.json()
    assert len(data['data']) == 2


def test_filter_by_user(session):
    trial_1 = {
        'user': '0001',
        'op_type': '3x1'
    }
    trial_2 = {
        'user': '0001',
        'op_type': '3x1'
    }
    trial_3 = {
        'user': '0003',
        'op_type': '3x3'
    }
    trials = [trial_1, trial_2, trial_3]
    for trial in trials:
        requests.post(URL_PREFIX + 'v2/trials', json=trial)
    r = requests.get(URL_PREFIX + 'v2/trials?user=0001')
    data = r.json()
    assert len(data['data']) == 2


def test_filter_by_user_and_op_type(session):
    trial_1 = {
        'user': '0001',
        'op_type': '3x1'
    }
    trial_2 = {
        'user': '0001',
        'op_type': '3x2'
    }
    trial_3 = {
        'user': '0002',
        'op_type': '3x1'
    }
    trial_4 = {
        'user': '0002',
        'op_type': '3x2'
    }
    trial_5 = {
        'user': '0001',
        'op_type': '3x1'
    }
    trials = [trial_1, trial_2, trial_3, trial_4, trial_5]
    for trial in trials:
        requests.post(URL_PREFIX + 'v2/trials', json=trial)
    r = requests.get(URL_PREFIX + 'v2/trials?op_type=3x1&user=0001')
    data = r.json()
    assert len(data['data']) == 2
