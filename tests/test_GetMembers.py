import pytest
import requests
from jsonschema import validate

from BaseTestOK import BaseTestOK


class TestGetFriends(BaseTestOK):
    method = 'group.getMembers'
    signature = ''

    count = '50'
    uid = '59381746499761'

    schema = {
        "type": "object",
        "properties": {
            "has_more": {"type": "boolean"},
            "anchor": {"type": "string"},
            "members": {
                "type": "array",
                "items":
                    {
                        "userId": "string"
                    }
            }
        }
    }

    @pytest.fixture(scope='class')
    def response(self):
        p = {'sig': self.signature,
             'application_key': self.application_key,
             'session_key': self.session_key,
             'method': self.method,
             'count': self.count,
             'uid': self.uid}

        r = requests.get(self.url, params=p)
        print('request sent')
        return r

    def test_all_content_type(self, response):
        assert response.headers["Content-Type"] == "application/json;charset=utf-8"

    def test_group_has_less_than_100_users(self, response):
        assert not response.json()['has_more']

    def test_next_id_is_greater(self, response):
        flag = False

        for i in range(len(response.json()['members']) - 1):
            if int(response.json()['members'][i]['userId']) < int(response.json()['members'][i + 1]['userId']):
                flag = True
            else:
                flag = False

        assert flag

    def test_schema_is_valid(self, response):
        validate(instance=response.json(), schema=self.schema)
