import importlib

import pytest

from frame.demo import hello
from frame.demo.context import Context


class TestMain:
    context = Context()
    context.load("./tmp.yaml")

    @pytest.mark.parametrize("testcase", context.store.testcase.values(), ids=context.store.testcase.keys())
    def test_main(self, testcase):
        self.context.run_steps_by_testcase(testcase)

    def test_tmp(self):
        # 动态导入hello模块
        c = importlib.import_module("hello")
        # 从c中反射拿到a方法并调用
        getattr(c, 'a')()

    def test(self):
        # 定义全局变量a
        globals()["a"] = 101
        # 打印全局变量a
        print(globals()["a"])
        # 判断hello模块是否有c方法
        print(hasattr(hello, 'c'))
        a = 1
        # 将string类型当成python命令调用
        print(eval("a"))
