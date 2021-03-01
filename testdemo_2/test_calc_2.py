import allure
import pytest
import yaml

from testdemo_2.calculator_2 import Calculator

# 判断输入是否为数字
from testdemo_2.conftest import get_calc


def is_number(a, b, expect):
    # str1, str2, str3 = str(a), str(b), str(expect)
    # num1 = str1.isdigit()
    # num2 = str2.isdigit()
    # num3 = str3.isdigit()
    [str1, str2, str3] = map(lambda x: str(x).isdigit(), [a, b, expect])
    if str1 == str2 == str3 is True:
        pass
    else:
        print("请输入数字")


# 获取测试数据
def get_datas():
    with open('./data/calc_data_2.yaml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    sub_datas = datas['sub']['datas']
    sub_ids = datas['sub']['ids']
    mul_datas = datas['mul']['datas']
    mul_ids = datas['mul']['ids']
    div_datas = datas['div']['datas']
    div_ids = datas['div']['ids']
    return [add_datas, add_ids, sub_datas, sub_ids, mul_datas, mul_ids, div_datas, div_ids]


class TestCalc:
    # def setup_method(self):
    #     print("计算开始")
    #     self.calcu = Calculator()
    #
    # def teardown_method(self):
    #     print("计算结束")

    @pytest.mark.run(order=0)
    @pytest.mark.parametrize('a, b, expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, get_calc, a, b, expect):
        print("加法")
        is_number(a, b, expect)  # 判断测试数据是否为数字
        # result = self.calcu.add(a, b)
        result = get_calc.add(a, b)
        assert round(result, 2) == expect  # 结果保留两位并与测试数据中期望值比较

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a, b, expect', get_datas()[2], ids=get_datas()[3])
    def test_sub(self, get_calc, a, b, expect):
        print("减法")
        # result = self.calcu.sub(a, b)
        result = get_calc.sub(a, b)
        assert round(result, 2) == expect

    @pytest.mark.run(order=-1)
    @pytest.mark.parametrize('a, b, expect', get_datas()[4], ids=get_datas()[5])
    def test_mul(self, get_calc, a, b, expect):
        print("乘法计算")
        # result = self.calcu.mul(a, b)
        result = get_calc.mul(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a, b, expect', get_datas()[6], ids=get_datas()[7])
    @pytest.mark.run(order=1)
    def test_div(self, get_calc, a, b, expect):
        print("除法计算")
        is_number(a, b, expect)
        try:
            if b == 0:
                raise ZeroDivisionError('0不能作为被除数')
        except Exception as e:
            print(e)
        else:
            # result = self.calcu.div(a, b)
            result = get_calc.div(a, b)
            assert round(result, 2) == expect
