from behave import *

from StudentMgmt import Environment
from StudentMgmt.Student import Student
from StudentMgmt.api import UpdateStudent
from StudentMgmt.tests.TestDataMap import TestData

use_step_matcher("re")


@when("update the student's (?P<field>.+)")
def step_impl(context, field):
    """
    :type context: behave.runner.Context
    :type field: str
    """
    td = TestData.value_of(field)
    student = context.student
    original_val = ""
    new_num = Environment.get_max_student_id_num() + 2
    if td == TestData.ID:
        original_val = student.get_id()
        student.set_id(new_num)
    elif td == TestData.FIRST_NAME:
        original_val = student.get_first_name()
        student.set_first_name(Student().get_first_name())
    elif td == TestData.LAST_NAME:
        original_val = student.get_last_name()
        student.set_last_name(Student().get_last_name())
    elif td == TestData.STUDENT_CLASS:
        original_val = student.get_student_class()
        student.set_student_class(Student().get_student_class())
    elif td == TestData.NATIONALITY:
        original_val = student.get_nationality()
        student.set_nationality(Student().get_nationality())
    elif td == TestData.MISSING_ID:
        original_val = student.get_id()
        student.set_id(None)
    elif td == TestData.MISSING_FIRST_NAME:
        original_val = student.get_first_name()
        student.set_first_name(None)
    elif td == TestData.MISSING_LAST_NAME:
        original_val = student.get_last_name()
        student.set_last_name(None)
    elif td == TestData.MISSING_CLASS_NAME:
        original_val = student.get_student_class()
        student.set_student_class(None)
    elif td == TestData.MISSING_NATIONALITY:
        original_val = student.get_nationality()
        student.set_nationality(None)
    else:
        raise Exception("Wrong/Missing input field")
    response = UpdateStudent.update_student(context.student)
    context.original_value = original_val
    context.response = response


@then("a student should not be updated with status code (?P<response_code>.+)")
def step_impl(context, response_code):
    """
    :type context: behave.runner.Context
    :type response_code: str
    """
    response = context.response
    status_code = response.status_code
    print(status_code)
    assert status_code == int(response_code)


@then("check with old values for (?P<field>.+)")
def step_impl(context, field):
    """
    :type context: behave.runner.Context
    :type field: str
    """
    response = context.response
    original_val = context.original_value
    td = TestData.value_of(field)
    if response.status_code == 200:
        json = response.json()
        if td == TestData.FIRST_NAME:
            assert original_val != json.get('firstName')
        elif td == TestData.LAST_NAME:
            assert original_val != json.get('lastName')
        elif td == TestData.STUDENT_CLASS:
            assert original_val != json.get('studentClass')
        elif td == TestData.NATIONALITY:
            assert original_val != json.get('nationality')
    elif td != TestData.ID and td != TestData.MISSING_ID:
        raise Exception("Failed Update")
