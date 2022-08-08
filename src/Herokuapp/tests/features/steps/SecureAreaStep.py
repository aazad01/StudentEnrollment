from behave import *

from Herokuapp.web.SecureArea import SecureArea

use_step_matcher("re")

secure = SecureArea()


@step("it was successful")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert 'You logged into a secure area!' in secure.get_alert()


@step("it loaded the Secure Area")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    secure.page_load()
    assert secure.get_header() == 'Secure Area'


@step("you can logout")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    secure.click_logout()
