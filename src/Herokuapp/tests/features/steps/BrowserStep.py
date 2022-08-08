from behave import *

import Environment
from Herokuapp.helper.Browser import *

use_step_matcher("re")


@given("browser loads url")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.get(Environment.WEB_UI)
