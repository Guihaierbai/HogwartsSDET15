# 自动调用conftest.py下存储的fixture
def test_case1(login):
    print("case1")


def test_case2():
    print("case2")


def test_case3(login, conn_db):
    print("case3")
