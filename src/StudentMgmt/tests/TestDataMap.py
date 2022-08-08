import enum

from StudentMgmt.Student import Student
from StudentMgmt.helper import Randoms


class TestData(enum.Enum):
    VALID_STUDENT = "Valid Student", True,
    INVALID_STUDENT = "Invalid Student", False,
    SUCCESSFULLY = "successfully", True,
    UNSUCCESSFULLY = "unsuccessfully", False,

    MISSING_ID = "Missing Id", Student().set_id(None),
    MISSING_FIRST_NAME = "Missing First Name", Student().set_first_name(None),
    MISSING_LAST_NAME = "Missing Last Name", Student().set_last_name(None),
    MISSING_CLASS_NAME = "Missing Class", Student().set_student_class(None),
    MISSING_NATIONALITY = "Missing Nationality", Student().set_nationality(None)

    MAX_CHAR_FIRST_NAME = "Max Character First Name", Student().set_first_name(Randoms.random_string(300)),
    MAX_CHAR_LAST_NAME = "Max Character Last Name", Student().set_last_name(Randoms.random_string(300)),
    MAX_CHAR_CLASS_NAME = "Max Character Class", Student().set_student_class(Randoms.random_string(300)),
    MAX_CHAR_NATIONALITY = "Max Character Nationality", Student().set_nationality(Randoms.random_string(300))
    SQL_INJECT = "SQL INJECT", Student().set_first_name(";Select * FROM all_tables")

    ID = "ID", True,
    FIRST_NAME = "First Name", True,
    LAST_NAME = "Last Name", True,
    NATIONALITY = "Nationality", True,
    STUDENT_CLASS = "Student Class", True,

    @classmethod
    def value_of(cls, value):
        return list(filter(lambda x: x.value[0] == value, TestData))[0]
