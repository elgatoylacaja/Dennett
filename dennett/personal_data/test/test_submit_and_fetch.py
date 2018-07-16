import pytest
import requests

from conftest import URL_PREFIX


@pytest.mark.usefixtures("session")
class TestSubmittingAndFetchingPersonalData(object):

    def test_post_personal_data(self):
        personal_data = {
            'Studies': 'College completed',
            'Gender': 'Male'
        }
        r = requests.post(URL_PREFIX + 'v2/personal-data', json=personal_data)
        assert r.status_code == 201

    def test_get_personal_data(self):
        r = requests.get(URL_PREFIX + 'v2/personal-data')
        data = r.json()
        assert r.status_code == 200
        assert len(data) == 0

        personal_data_items = [
            {'Studies': 'College completed', 'Gender': 'Male'},
            {'Studies': 'College completed', 'Gender': 'Female'},
            {'Studies': 'University completed', 'Gender': 'Male'},
        ]
        requests.post(URL_PREFIX + 'v2/personal-data', json=personal_data_items)

        data = requests.get(URL_PREFIX + 'v2/personal-data').json()
        assert len(data) == 3
