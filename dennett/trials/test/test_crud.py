import pytest
import requests

from conftest import URL_PREFIX


@pytest.mark.usefixtures("session")
class TestCrud(object):

    def test_post_trial(self):
        trial = {
            'user': '0001',
            'op_type': '3x2'
        }
        r = requests.post(URL_PREFIX + 'v1/trials', json=trial)
        assert r.status_code == 201

    def test_get_empty_trials_list(self):
        r = requests.get(URL_PREFIX + 'v1/trials')
        data = r.json()
        assert r.status_code == 200
        assert len(data) == 0

    def test_get_trials_list(self):
        trials = [
            {'user': '0001', 'op_type': '3x1'},
            {'user': '0002', 'op_type': '3x2'},
            {'user': '0003', 'op_type': '3x3'}
        ]
        for trial in trials:
            requests.post(URL_PREFIX + 'v1/trials', json=trial)
        data = requests.get(URL_PREFIX + 'v1/trials').json()
        assert len(data) == 3
