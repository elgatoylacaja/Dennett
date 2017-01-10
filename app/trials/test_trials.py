import requests
from flask import url_for
from conftest import session, URL_PREFIX


def test_get_trials_list(session):
    r = requests.get(URL_PREFIX + 'trials')
    assert r.status_code == 200
