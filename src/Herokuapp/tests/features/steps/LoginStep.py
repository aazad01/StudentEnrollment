from behave import *

from Herokuapp.web.LoginPage import LoginPage
from helper import Randoms

use_step_matcher("re")

login = LoginPage()


@when("browser is done loading")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    login.page_load()


@then("check if everything has loaded")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert login.get_header() == 'Login Page'
    assert login.get_subheader() == 'This is where you can log into the secure area. Enter tomsmith for the username and ' \
                                    'SuperSecretPassword! for the password. If the information is wrong you should see error messages.'


@step("you can login")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    login.enter_username(context.usr.get('username'))
    login.enter_password(context.usr.get('password'))
    login.click_submit()


@given("valid user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.usr = {'username': 'tomsmith', 'password': 'SuperSecretPassword!'}


# @step("you get an error")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     assert login.error.is_displayed()
#     assert login.error.text == z


@step("logout alert is displayed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert 'You logged out of the secure area!' in login.get_alert()


@given("a wrong (?P<user>.+)")
def step_impl(context, user):
    """
    :type context: behave.runner.Context
    :type user: str
    """
    if user == 'Username':
        context.usr = {'username': 'tom', 'password': 'SuperSecretPassword!'}
    elif user == 'Password':
        context.usr = {'username': 'tomsmith', 'password': 'Password!'}
    else:
        context.usr = {'username': Randoms.random_string(100), 'password': Randoms.random_string(100)}


@step("you get an error: (?P<error>.+)")
def step_impl(context, error):
    """
    :type context: behave.runner.Context
    :type error: str
    """
    if error == 'Invalid Username':
        assert "Your username is invalid!" in login.get_alert()
    elif error == 'Invalid Password':
        assert "Your password is invalid!" in login.get_alert()
    else:
        raise Exception(f"Not handled error: {login.get_alert()}")
