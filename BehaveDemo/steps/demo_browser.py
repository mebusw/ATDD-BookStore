#!encoding=utf8
from behave import *
from hamcrest import *
import sure
from ..browser import Browser
from selenium import webdriver

use_step_matcher("re")

# def before_all(context):
#     context.browser = Browser()

# def after_all(context):
#     context.browser.close()


@given(u"我已具有网站账号")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser = Browser()
    context.browser.base_url = 'https://www.bing.com'
    context.browser.visit('/')

@when(u"我使用用户名(?P<username>.+)和密码(?P<password>.+)登录网站")
def step_impl(context, username, password):
    q = context.browser.find_by_id('sb_form_q')
    q.send_keys(u'优普丰')
    btn = context.browser.find_by_id('sb_form_go')
    btn.click()
    
    
    

@then(u"网站跳转到首页")
def step_impl(context):
    context.browser.page_should_contain(u'uperform')
    context.browser.close()
