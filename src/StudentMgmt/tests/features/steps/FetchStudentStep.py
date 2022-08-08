from behave import *

from StudentMgmt.api import FetchStudent

use_step_matcher("re")


@step("a student exists")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    student = context.student
    response = FetchStudent.fetch_student(student.get_id(), student.get_student_class())
    json = response.json()
    assert len(response.json()) == 1
    assert json[0].get('id') == student.get_id()
    assert json[0].get('studentClass') == student.get_student_class()
    assert json[0].get('firstName') == student.get_first_name()
    assert json[0].get('lastName') == student.get_last_name()
    assert json[0].get('nationality') == student.get_nationality()


@step("a student does NOT exists")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    student = context.student
    response = FetchStudent.fetch_student(student.get_id(), student.get_student_class())
    assert len(response.json()) == 0
