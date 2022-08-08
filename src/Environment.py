LOCAL_HOST = "localhost"
PORT = 9080
BASE_URL = f"http://{LOCAL_HOST}:{PORT}/studentmgmt/"
ADD_END_POINT = "addStudent"
DELETE_END_POINT = "deleteStudent"
FETCH_END_POINT = "fetchStudents"
UPDATE_END_POINT = "updateStudent"

# Probably should be moved to it's own class maybe as School.
num = 0


def get_max_student_id_num():
    return num


WEB_UI = "https://the-internet.herokuapp.com/login"
