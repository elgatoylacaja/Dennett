import pytest
import requests

from conftest import URL_PREFIX

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


@pytest.mark.usefixtures("session")
class TestFiltersAndPagination(object):
    # v1 tests

    def test_pagination_v1(self):
        self._test_pagination('v1')

    def test_cron_and_pagination_v1(self):
        self._test_cron_and_pagination('v1')

    def test_cron_old_v1(self):
        self._test_cron_old('v1')

    def test_cron_new_v1(self):
        self._test_cron_new('v1')

    # v2 tests

    def test_pagination_v2(self):
        self._test_pagination('v2')

    def test_cron_and_pagination_v2(self):
        self._test_cron_and_pagination('v2')

    def test_cron_old_v2(self):
        self._test_cron_old('v2')

    def test_cron_new_v2(self):
        self._test_cron_new('v2')

    # helpers

    def _test_pagination(self, api_version_prefix='v1'):
        for trial in TRIALS:
            requests.post(URL_PREFIX + api_version_prefix + '/trials', json=trial)
        data = requests.get(URL_PREFIX + api_version_prefix + '/trials?size=2&page=2').json()
        assert len(data) == 2
        assert data[0]['id'] == '3'
        assert data[1]['id'] == '4'

    def _test_cron_and_pagination(self, api_version_prefix='v1'):
        for trial in TRIALS:
            requests.post(URL_PREFIX + api_version_prefix + '/trials', json=trial)
        data = requests.get(URL_PREFIX + api_version_prefix + '/trials?cron=new&size=2&page=2').json()
        assert len(data) == 2
        assert data[0]['id'] == '10'
        assert data[1]['id'] == '9'

    def _test_cron_old(self, api_version_prefix='v1'):
        for trial in TRIALS:
            requests.post(URL_PREFIX + api_version_prefix + '/trials', json=trial)
        data = requests.get(URL_PREFIX + api_version_prefix + '/trials').json()
        assert data[0]['id'] == '1'
        assert data[1]['id'] == '2'
        assert data[2]['id'] == '3'

    def _test_cron_new(self, api_version_prefix='v1'):
        for trial in TRIALS:
            requests.post(URL_PREFIX + api_version_prefix + '/trials', json=trial)
        data = requests.get(URL_PREFIX + api_version_prefix + '/trials?cron=new').json()
        assert data[0]['id'] == '12'
        assert data[1]['id'] == '11'
        assert data[2]['id'] == '10'
