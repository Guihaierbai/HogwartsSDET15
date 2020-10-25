import pytest


@pytest.fixture()
def login():
    # set up
    print("登陆操作")
    yield
    # teardown
    print("登出操作")


@pytest.fixture()
def conn_db():
    print("连接数据库")
