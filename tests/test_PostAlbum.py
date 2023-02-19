import pytest
import requests

from BaseTestOK import BaseTestOK


class TestPostAlbum(BaseTestOK):
    method = 'photos.createAlbum'
    signature = ''

    title = 'test_album'
    type = 'PRIVATE'

    @pytest.mark.skip(reason="xd")
    def test_12_digits_response(self):
        p = {'sig': self.signature,
             'application_key': self.application_key,
             'session_key': self.session_key,
             'method': self.method,
             'title': self.title,
             'type': self.type}

        r = requests.post(self.url, params=p)
        response_body = r.json()

        assert len(str(response_body)) == 12
        assert r.status_code == 200
