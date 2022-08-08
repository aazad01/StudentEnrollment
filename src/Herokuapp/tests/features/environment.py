from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from Herokuapp.helper import Browser


@fixture
def selenium_browser(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    context.driver.implicitly_wait(2)
    context.driver.maximize_window()
    Browser.driver = context.driver

    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver.quit()


def before_all(context):
    use_fixture(selenium_browser, context)
    # -- HINT: CLEANUP-FIXTURE is performed after after_all() hook is called.
