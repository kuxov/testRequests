import pytest
import requests

from BaseTestOK import BaseTestOK


class TestGetFriends(BaseTestOK):
    method = 'friends.get'
    signature = ''

    def test_only_one_friend_lisa(self):
        p = {'sig': self.signature,
             'application_key': self.application_key,
             'session_key': self.session_key,
             'method': self.method}

        r = requests.get(self.url, params=p)

        assert r.status_code == 200
        assert r.text == '["579385361227"]'

    def test_only_one_friend_lisa_no_session_key(self):
        p = {'sig': self.signature,
             'application_key': self.application_key,
             'method': self.method}

        r = requests.get(self.url, params=p)
        response_body = r.json()

        assert response_body["error_code"] == 9
        assert "IP_BLOCKED" in response_body["error_msg"]
        assert not response_body["error_data"]


