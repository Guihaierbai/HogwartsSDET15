import jsonpath
import requests
from hamcrest.core import assert_that


class TestDemo:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
