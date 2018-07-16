import pytest
import requests

from conftest import URL_PREFIX


@pytest.mark.usefixtures("session")
class TestSubmittingAndFetchingTrials(object):

    # v1 tests

    def test_post_trial_v1(self):
        self._test_post_trial('v1')

    def test_get_empty_trials_list_v1(self):
        self._test_get_empty_trials_list('v1')

    def test_get_trials_list_v1(self):
        self._test_get_trials_list('v1')

    # v2 tests

    def test_post_multiple_trials(self):
        trials = [
            {
                'user': '0001',
                'op_type': '3x2'
            },
            {
                'user': '0001',
                'op_type': '3x8'
            },
        ]
        r = requests.post(URL_PREFIX + 'v2/trials', json=trials)
        assert r.status_code == 201

    def test_post_trial_v2(self):
        self._test_post_trial('v2')

    def test_get_empty_trials_list_v2(self):
        self._test_get_empty_trials_list('v2')

    def test_get_trials_list_v2(self):
        self._test_get_trials_list('v2')

    # helpers

    def _test_post_trial(self, api_version_prefix='v1'):
        trial = {
            'user': '0001',
            'op_type': '3x2'
        }
        r = requests.post(URL_PREFIX + api_version_prefix + '/trials', json=trial)
        assert r.status_code == 201

    def _test_get_empty_trials_list(self, api_version_prefix='v1'):
        r = requests.get(URL_PREFIX + api_version_prefix + '/trials')
        data = r.json()
        assert r.status_code == 200
        assert len(data) == 0

    def _test_get_trials_list(self, api_version_prefix='v1'):
        trials = [
            {'user': '0001', 'op_type': '3x1'},
            {'user': '0002', 'op_type': '3x2'},
            {'user': '0003', 'op_type': '3x3'}
        ]
        for trial in trials:
            requests.post(URL_PREFIX + api_version_prefix + '/trials', json=trial)
        data = requests.get(URL_PREFIX + api_version_prefix + '/trials').json()
        assert len(data) == 3
