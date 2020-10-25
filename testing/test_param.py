import pytest


@pytest.mark.parametrize('b', [4, 5, 6])
@pytest.mark.parametrize('a', [4, 5, 6])
def test_parm(a, b):
    print(a, b)
