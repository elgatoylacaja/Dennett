import requests
from conftest import session, URL_PREFIX


def test_filter_by_op_type(session):
    trials_selected = [
        {'user': '0001', 'op_type': '3x1'},
        {'user': '0002', 'op_type': '3x1'}
    ]
    trials_rejected = [
        {'user': '0001', 'op_type': '3x4'},
        {'user': '0002', 'op_type': '3x2'},
        {'user': '0003', 'op_type': '3x3'}
    ]
    for trial in trials_selected + trials_rejected:
        requests.post(URL_PREFIX + 'v2/trials', json=trial)
    data = requests.get(URL_PREFIX + 'v2/trials?op_type=3x1').json()
    for trial in trials_selected:
        assert trial in data['data']
    for trial in trials_rejected:
        assert trial not in data['data']


def test_filter_by_user(session):
    trials_selected = [
        {'user': '0001', 'op_type': '3x1'},
        {'user': '0001', 'op_type': '3x1'}
    ]
    trials_rejected = [
        {'user': '0002', 'op_type': '3x1'},
        {'user': '0002', 'op_type': '3x2'},
        {'user': '0003', 'op_type': '3x3'}
    ]
    for trial in trials_selected + trials_rejected:
        requests.post(URL_PREFIX + 'v2/trials', json=trial)
    data = requests.get(URL_PREFIX + 'v2/trials?user=0001').json()
    for trial in trials_selected:
        assert trial in data['data']
    for trial in trials_rejected:
        assert trial not in data['data']


def test_filter_by_user_and_op_type(session):
    trials_selected = [
        {'user': '0001', 'op_type': '3x1'},
        {'user': '0001', 'op_type': '3x1'}
    ]
    trials_rejected = [
        {'user': '0002', 'op_type': '3x1'},
        {'user': '0002', 'op_type': '3x2'},
        {'user': '0001', 'op_type': '3x2'}
    ]
    for trial in trials_selected + trials_rejected:
        requests.post(URL_PREFIX + 'v2/trials', json=trial)
    data = requests.get(URL_PREFIX + 'v2/trials?op_type=3x1&user=0001').json()
    for trial in trials_selected:
        assert trial in data['data']
    for trial in trials_rejected:
        assert trial not in data['data']
