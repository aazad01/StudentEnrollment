import time

from behave import *

use_step_matcher("re")
WEB_UI = "https://the-internet.herokuapp.com/login"


@given("browser loads url")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    time.sleep(2)
    context.driver.get(WEB_UI)
