import pytest


@pytest.mark.login
def test_login1():
    print("登陆用例")


@pytest.mark.login
def test_login2():
    print("登陆用例")


@pytest.mark.login
def test_login3():
    print("登陆用例")


@pytest.mark.search
def test_search1():
    print("搜索用例")


@pytest.mark.search
def test_search2():
    print("搜索用例")


@pytest.mark.search
def test_search3():
    print("搜索用例")
