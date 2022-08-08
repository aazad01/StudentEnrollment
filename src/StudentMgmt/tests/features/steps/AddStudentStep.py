from behave import *

from StudentMgmt.api.AddStudent import AddStudent
from StudentMgmt.tests.TestDataMap import TestData

use_step_matcher("re")

add_api = AddStudent()


@when("I try to add a (?P<student>.+)")
def step_impl(context, student):
    """
    :type context: behave.runner.Context
    :type student: str
    """
    if TestData.value_of(student):
        context.student.set_id(len(context.school))
    context.response = add_api.add_student(context.student)


@then("a student is (?P<success>.+) added")
def step_impl(context, success):
    """
    :type context: behave.runner.Context
    :type success: str
    """
    assert context.response.status_code == (200 if TestData.value_of(success) else 500)


@given("missing (?P<data>.+)")
def step_impl(context, data):
    """
    :type context: behave.runner.Context
    :type data: str
    """
    td = TestData.value_of(data)
    context.student = td.value[1]
    if td != TestData.MISSING_ID:
        context.student.set_id(len(context.school))
    print(td.value[0])


@when("I try to add the student")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = add_api.add_student(context.student)


@then("a student should not be added with (?P<response_code>.+)")
def step_impl(context, response_code):
    """
    :type context: behave.runner.Context
    :type response_code: str
    """
    print(context.response.status_code)
    assert context.response.status_code == int(response_code)
