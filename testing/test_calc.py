import pytest

from pythoncode.calculator import Calculator


class TestCalc:

    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a, b, expect', [
        [1, 1, 2], [100, 100, 200], [0.1, 0.1, 0.2]
    ], ids=['int_case', 'bignum_case', 'float_case'])
    def test_add(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    def test_add1(self):
        test_data = [
            [1, 1, 2], [100, 100, 200], [0.1, 0.1, 0.2]]
        for i in range(0, len(test_data)):
            # calc = Calculator()
            result = self.calc.add(test_data[i][0], test_data[i][1])
            assert result == test_data[i][2]
    #
    # def test_add2(self):
    #     #calc = Calculator()
    #     result = self.calc.add(0.1,0.1)
    #     assert result == 0.2
