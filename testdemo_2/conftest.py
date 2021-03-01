import pytest

from testdemo_2.calculator_2 import Calculator


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope='module')
def get_calc():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("计算结束")
