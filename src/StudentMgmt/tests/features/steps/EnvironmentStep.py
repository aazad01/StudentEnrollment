import requests
from behave import *

from StudentMgmt import Environment
from StudentMgmt.Student import Student


@given("server is running")
def step_impl(context):
    response = requests.get(url=Environment.BASE_URL + Environment.FETCH_END_POINT)
    try:
        if response.status_code != 200:
            raise ConnectionError("Server isn't up")
        else:
            print("localhost server is up and running")
            context.school = response.json()
            Environment.num = max(list(map(lambda c: c.get('id'), context.school)))
    except Exception:
        raise ConnectionError("Server isn't up")


@given("create a {student}")
def step_impl(context, student):
    """
    :type context: behave.runner.Context
    :type student: str
    """
    context.student = Student()
