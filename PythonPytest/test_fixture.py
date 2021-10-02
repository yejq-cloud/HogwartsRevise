"""
hogwarts 
yejq
"""
import logging
import allure
import pytest


class TestCalculator():

   #使用装饰器添加标签
    @pytest.mark.add
    @allure.feature("加法-整数类型测试")
    def test_add_int(self, use_fixture,get_datas_addint):
        logging.info("===进入加法运算测试--整数类型===")
        assert get_datas_addint[2] == round(use_fixture.add(get_datas_addint[0], get_datas_addint[1]), 2)


    @pytest.mark.add
    @allure.feature("加法-浮点类型测试")
    def test_add_float(self, use_fixture, get_datas_addfloat):
        logging.info("===进入加法运算测试--浮点类型===")
        assert get_datas_addfloat[2] == round(use_fixture.add(get_datas_addfloat[0], get_datas_addfloat[1]), 2)


    @pytest.mark.add
    @allure.feature("加法-负数类型测试")
    def test_add_negative(self, use_fixture, get_datas_addnegative):
        logging.info("===进入加法运算测试--负数类型===")
        assert get_datas_addnegative[2] == round(use_fixture.add(get_datas_addnegative[0], get_datas_addnegative[1]), 2)


    @pytest.mark.minus
    @allure.feature("减法各数据类型测试")
    def test_minus(self, use_fixture, get_datas_minus):
        logging.info("===进入减法运算测试===")
        assert get_datas_minus[2] == use_fixture.minus(get_datas_minus[0], get_datas_minus[1])


    @allure.feature("乘法各数据类型测试")
    def test_mult(self, use_fixture, get_datas_mult):
        logging.info("===进入乘法运算测试===")
        assert get_datas_mult[2] == round(use_fixture.mult(get_datas_mult[0], get_datas_mult[1]), 2)


    @allure.feature("除法各类型测试")
    def test_div(self, use_fixture, get_datas_div):
        logging.info("===进入除法运算测试===")
        assert get_datas_div[2] == use_fixture.div(get_datas_div[0], get_datas_div[1])


    @allure.feature("除法除数为0测试")
    def test_div_zero(self, use_fixture):
        logging.info("===进入除法除数为0运算测试===")
        with pytest.raises(ZeroDivisionError):
            assert 0 == use_fixture.div(1, 0)
