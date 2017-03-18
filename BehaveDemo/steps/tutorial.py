#!encoding=utf8
from behave import *
from hamcrest import *
import sure

use_step_matcher("re")

con = []


@given("we have behave installed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('we implement a test')
def step_impl(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


@given('a set of specific users')
def step_impl(context):
    for row in context.table:
        con.append((row['name'], row['department']))


@when('login with')
def step_impl(context):
    pass


th = ''


@given("I put (?P<thing>.+) in a blender,")
def step_impl(context, thing):
    """
    :type context: behave.runner.Context
    :type thing: str
    """
    global th
    th = thing


@then('it should transform into (?P<other_thing>.+)')
def step_impl(context, other_thing):
    other_thing.should.be.equal('toxic waste')
    assert_that(other_thing, equal_to('toxic waste'))


@then('I call some other steps')
def step_impl(context):
    context.execute_steps(u'''
        then I duck
    ''')


@then('I duck')
def step_impl(context):
    assert True


