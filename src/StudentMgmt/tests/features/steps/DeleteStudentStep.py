from behave import *

from StudentMgmt.api import DeleteStudent

use_step_matcher("re")


@step("the student is (?P<success>.+) deleted")
def step_impl(context, success):
    """
    :type context: behave.runner.Context
    :type success: str
    """
    response = DeleteStudent.delete_student(context.student.get_id())
    assert response.status_code == 200
