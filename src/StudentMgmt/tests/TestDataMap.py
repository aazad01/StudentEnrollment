import enum

from StudentMgmt.Student import Student


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

    @classmethod
    def valueOf(cls, value):
        return list(filter(lambda x: x.value[0] == value, TestData))[0]
