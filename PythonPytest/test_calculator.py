"""
hogwarts 
yejq
"""
import logging

import allure
import yaml
from PythonPytest.calculator import Calculator
import pytest

def getdatas():
    logging.info("===进入获取测试数据===")
    with open('dates.yaml') as f:
        datas = yaml.safe_load(f)
    return datas

class TestCalculator():

    #运用setup_class/teardown_class级别，只需要在类的层面初始化一下，比方法级别更节省资源
    def setup_class(self):
        logging.info("===进入测试资源准备===")
        #实例化被测代码的类，前面加self，方便类里面其他方法调用
        self.calc = Calculator()
    def teardown_class(self):
        logging.info("===进入获取测试数据===")


    #使用装饰器添加标签
    @pytest.mark.add
    @pytest.mark.parametrize(
        'a,b,expect',
        getdatas()['add']['int']['datas'],
        ids=getdatas()['add']['int']['ids']
    )
    @allure.feature("加法-整数类型测试")
    def test_add_int(self, a, b, expect):
        logging.info("===进入加法运算测试--整数类型===")
        assert expect == round(self.calc.add(a, b), 2)


    @pytest.mark.add
    @pytest.mark.parametrize(
        'a,b,expect',
        getdatas()['add']['float']['datas'],
        ids = getdatas()['add']['float']['ids']
    )
    @allure.feature("加法-浮点类型测试")
    def test_add_float(self, a, b, expect):
        logging.info("===进入加法运算测试--浮点类型===")
        assert expect == round(self.calc.add(a, b), 2)


    @pytest.mark.add
    @pytest.mark.parametrize(
        'a,b,expect',
        getdatas()['add']['negative']['datas'],
        ids = getdatas()['add']['negative']['ids']
    )
    @allure.feature("加法-负数类型测试")
    def test_add_negative(self, a, b, expect):
        logging.info("===进入加法运算测试--负数类型===")
        assert expect == round(self.calc.add(a, b), 2)


    @pytest.mark.minus
    @pytest.mark.parametrize(
        'a,b,expect',
        getdatas()['minus']['datas'],
        ids = getdatas()['minus']['ids']
    )
    @allure.feature("减法各数据类型测试")
    def test_minus(self, a, b, expect):
        logging.info("===进入减法运算测试===")
        assert expect == self.calc.minus(a, b)


    @pytest.mark.parametrize(
        'a,b,expect',
        getdatas()['mult']['datas'],
        ids=getdatas()['mult']['ids']

    )
    @allure.feature("乘法各数据类型测试")
    def test_mult(self, a, b, expect):
        logging.info("===进入乘法运算测试===")
        assert expect == round(self.calc.mult(a, b), 2)


    @pytest.mark.parametrize(
        'a,b,expect',
        getdatas()['div']['datas'],
        ids=getdatas()['div']['ids']
    )
    @allure.feature("除法各类型测试")
    def test_div(self, a, b, expect):
        logging.info("===进入除法运算测试===")
        assert expect == self.calc.div(a, b)

    @allure.feature("除法除数为0测试")
    def test_div_zero(self):
        logging.info("===进入除法除数为0运算测试===")
        with pytest.raises(ZeroDivisionError):
            assert 0 == self.calc.div(1, 0)
