import pytest
import yaml

from pythoncode.calculator import Calculator


def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    print(add_ids)
    print(add_datas)
    return [add_datas, add_ids]


class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    # @pytest.mark.parametrize('a, b, expect', [
    #     [1, 1, 2], [100, 100, 200], [0.1, 0.1, 0.2]
    # ], ids=['int_case', 'bignum_case', 'float_case'])
    @pytest.mark.parametrize('a, b, expect', get_datas()[0], ids=get_datas()[1])
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

    @pytest.mark.parametrize('a, b', [
        [1, 0], [10, 0]
    ])
    def test_div(self, a, b):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a, b)
    #
    # def test_add2(self):
    #     #calc = Calculator()
    #     result = self.calc.add(0.1,0.1)
    #     assert result == 0.2
