import pytest
import yaml


class Testdata:
    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./data.yaml")))
    def test_data(self, a, b):
        print(a + b)
