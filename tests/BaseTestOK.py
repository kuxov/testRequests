import pytest
import requests


class BaseTestOK:
    application_key = ')'
    session_key = ')'
    url = 'https://api.ok.ru/fb.do'
    method: str
    sig: str

