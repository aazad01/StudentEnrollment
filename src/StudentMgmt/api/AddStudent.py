import requests

import environment
from StudentMgmt import Student


def add_student_detail(id, first_name, last_name, nationality, student_class):
    payload = {
        "firstName": first_name,
        "id": id,
        "lastName": last_name,
        "nationality": nationality,
        "studentClass": student_class
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(environment.BASE_URL + environment.ADD_END_POINT, json=payload, headers=headers)
    print(response.text)
    return response


def add_student(student: Student):
    return add_student_detail(student.get_id(), student.get_first_name(), student.get_last_name(),
                              student.get_nationality(),
                              student.get_student_class())
