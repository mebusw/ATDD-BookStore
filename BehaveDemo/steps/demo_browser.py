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

@when(u"我搜索(?P<keyword>.+)关键字")
def step_impl(context, keyword):
    q = context.browser.find_by_id('sb_form_q')
    q.send_keys(keyword)
    btn = context.browser.find_by_id('sb_form_go')
    btn.click()
    
    
@then(u"网站显示包括(?P<keyword>.+)")
def step_impl(context, keyword):
    context.browser.page_should_contain(keyword)
    context.browser.close()
