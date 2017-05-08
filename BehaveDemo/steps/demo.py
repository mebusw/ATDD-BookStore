#!encoding=utf8
from behave import *
from hamcrest import *
import sure

use_step_matcher("re")

success_logged_in = False


@given(u"我已具有亚马逊账号")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

@when(u"我使用用户名(?P<username>.+)和密码(?P<password>.+)进行登录")
def step_impl(context, username, password):
    global success_logged_in
    success_logged_in = username == 'JackyShen@UPerform.CN' and password =='Abc12345'


@then(u"系统跳转到首页")
def step_impl(context):
    assert success_logged_in    

@then(u"提示用户名格式有误")
def step_impl(context):
    assert success_logged_in is False 

@then(u"提示密码格式有误")
def step_impl(context):
    assert success_logged_in is False 
