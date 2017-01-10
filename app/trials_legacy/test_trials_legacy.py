import requests
from conftest import session, URL_PREFIX


def test_post_trial_legacy(session):
    trial = {
        'user': '0001',
        'type': '3x2'
    }
    r = requests.post(URL_PREFIX + 'v1/trials', json=trial)
    assert r.status_code == 201
    data = r.json()
    assert data['user'] == trial['user']
    assert data['type'] == trial['type']
