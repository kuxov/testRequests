import pytest
import requests

from BaseTestOK import BaseTestOK


class TestDeleteAlbum(BaseTestOK):
    method = 'photos.deleteAlbum'
    signature = ''

    @pytest.mark.skip(reason="xd")
    @pytest.mark.parametrize('aid', ['951468074293',
                                     '951467806005',
                                     '949547011637'])
    def test_delete_album(self, aid):
        p = {'sig': self.signature,
             'application_key': self.application_key,
             'session_key': self.session_key,
             'method': self.method,
             'aid': aid}

        r = requests.delete(self.url, params=p)

        assert r.status_code == 200
