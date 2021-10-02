"""
hogwarts 
yejq
"""
import logging
import pytest
import yaml
from PythonPytest.calculator import Calculator


@pytest.fixture(scope="class")
def use_fixture():
    logging.info("===进入测试资源准备===")
    calc = Calculator()
    yield calc
    logging.info("===进入回收测试资源===")

def getdatas():
    logging.info("===进入获取测试数据===")
    with open('dates.yaml') as f:
        datas = yaml.safe_load(f)
    return datas

@pytest.fixture(
    params=getdatas()['add']['int']['datas'] ,
    ids=getdatas()['add']['int']['ids']
)
def get_datas_addint(request):
    return request.param

@pytest.fixture(
    params=getdatas()['add']['float']['datas'],
    ids=getdatas()['add']['float']['ids']
)
def get_datas_addfloat(request):
    return request.param

@pytest.fixture(
    params=getdatas()['add']['negative']['datas'],
    ids=getdatas()['add']['negative']['ids']
)
def get_datas_addnegative(request):
    return request.param

@pytest.fixture(
    params=getdatas()['minus']['datas'],
    ids=getdatas()['minus']['ids']
)
def get_datas_minus(request):
    return request.param

@pytest.fixture(
    params=getdatas()['mult']['datas'],
    ids=getdatas()['mult']['ids']
)
def get_datas_mult(request):
    return request.param

@pytest.fixture(
    params=getdatas()['div']['datas'],
    ids=getdatas()['div']['ids']
)
def get_datas_div(request):
    return request.param