import pytest
import requests

from conftest import URL_PREFIX


@pytest.mark.usefixtures("session")
class TestStats(object):

    def test_get_stats(self):
        stats = requests.get(URL_PREFIX + 'v1/stats').json()
        assert stats['trials'] == 0

        trials = [
            {'experiment_log': {'PersonalData': {'AUID': '0001', 'Name': 'A'}}, 'op_type': '3x1'},
            {'experiment_log': {'PersonalData': {'AUID': '0001', 'Name': 'B'}}, 'op_type': '3x2'},
            {'experiment_log': {'PersonalData': {'AUID': '0001', 'Name': 'C'}}, 'op_type': '3x3'},
            {'experiment_log': {'PersonalData': {'AUID': '0003', 'Name': 'D'}}, 'op_type': '3x4'},
            {'experiment_log': {'PersonalData': {'AUID': '0004', 'Name': 'E'}}, 'op_type': '3x5'}
        ]
        for trial in trials:
            requests.post(URL_PREFIX + 'v1/trials', json=trial)
        stats = requests.get(URL_PREFIX + 'v1/stats').json()
        assert stats['trials'] == 5
