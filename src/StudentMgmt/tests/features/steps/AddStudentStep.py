import random

from behave import *

from StudentMgmt import Environment
from StudentMgmt.api import AddStudent
from StudentMgmt.tests.TestDataMap import TestData

use_step_matcher("re")


@when("I try to add a (?P<student>.+)")
def step_impl(context, student):
    """
    :type context: behave.runner.Context
    :type student: str
    """
    print(context.student.get_last_name())
    if TestData.value_of(student).value[1]:
        context.student.set_id(Environment.get_max_student_id_num() + 1)
    else:
        context.student.set_id(random.choice(list(map(lambda c: c.get('id'), context.school))))
    context.response = AddStudent.add_student(context.student)
    print(f"{context.student.get_first_name()} {context.student.get_last_name()}")


@then("a student is (?P<success>.+) added")
def step_impl(context, success):
    """
    :type context: behave.runner.Context
    :type success: str
    """
    assert context.response.status_code == (200 if TestData.value_of(success).value[1] else 500)


@given("missing (?P<data>.+)")
def step_impl(context, data):
    """
    :type context: behave.runner.Context
    :type data: str
    """
    td = TestData.value_of(data)
    context.student = td.value[1]
    if td != TestData.MISSING_ID:
        context.student.set_id(Environment.get_max_student_id_num() + 1)
    print(td.value[0])


@when("I try to add the student")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = AddStudent.add_student(context.student)


@then("a student should not be added with status code (?P<response_code>.+)")
def step_impl(context, response_code):
    """
    :type context: behave.runner.Context
    :type response_code: str
    """
    print(context.response.status_code)
    assert context.response.status_code == int(response_code)


@step("the student can't be added again")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = AddStudent.add_student(context.student)
    assert context.response.status_code == 500
    assert 'Student already exists' in context.response.text
