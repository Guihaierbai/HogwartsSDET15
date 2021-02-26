import pytest

from testdemo_2.calculator_2 import Calculator


class TestCalc:
    def setup_method(self):
        print("计算开始")
        self.calcu = Calculator()

    def teardown_method(self):
        print("计算结束")

    # 判断输入是否为数字
    def is_number(self, a, b, expect):
        # str1, str2, str3 = str(a), str(b), str(expect)
        # num1 = str1.isdigit()
        # num2 = str2.isdigit()
        # num3 = str3.isdigit()
        [str1, str2, str3] = map(lambda x: str(x).isdigit(), [a, b, expect])
        if str1 == str2 == str3 is True:
            pass
        else:
            print("请输入数字")

    @pytest.mark.parametrize('a, b, expect', [
        [10, 20, 30], [200, 100, 300], [0.3, 0.5, 'a']
    ], ids=['int_case', 'bignum_case', 'float_case'])
    def test_add(self, a, b, expect):
        self.is_number(a, b, expect)
        result = self.calcu.add(a, b)
        assert result == expect

    def test_sub(self, a, b, expect):
        result = self.calcu.sub(a, b)
        assert result == expect

    def test_mul(self, a, b, expect):
        result = self.calcu.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', [
        [10, 0, 30], [200, 100, 2], [0.3, 0.5, 'a']
    ], ids=['int_case', 'bignum_case', 'float_case'])
    def test_div(self, a, b, expect):
        self.is_number(a, b, expect)
        try:
            if b == 0:
                raise ZeroDivisionError('0不能作为被除数')
        except Exception as e:
            print(e)
        else:
            result = self.calcu.div(a, b)
            assert result == expect
