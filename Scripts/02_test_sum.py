import pytest, os, yaml, sys
sys.path.append(os.getcwd())
from Data.getData import GetData

def get_sum_data():
    # 定义存储数据列表
    sum_list = []
    # 读取sum.yml数据
    data = GetData().get_yml_data("sum.yml")
    for i in data.values():
        sum_list.append(tuple(i.values()))
    return sum_list


"""
data={
    "test_sum1": {"a": 1, "b": 2,"c": 3}
    "test_sum2": {"a": 2, "b": 3,"c": 5}
    "test_sum1": {"a": 4, "b": 5,"c": 7}}
"""


class TestSum:
    @pytest.mark.parametrize("a,b,c", get_sum_data())
    def test_sum(self, a, b, c):
        print("{}+{}={}".format(a, b, c))
        assert a + b == c
