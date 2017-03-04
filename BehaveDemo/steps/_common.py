from behave import *
from hamcrest import *


@given('I commonly logged-in as {username}')
def step_impl(context, username):
    assert_that('Jacky', equal_to(username))
