import requests

from StudentMgmt import Environment, Student


def update_student_detail(id: int, first_name: str, last_name: str, nationality: str, student_class: str):
    payload = {
        "id": id,
        "firstName": first_name,
        "lastName": last_name,
        "studentClass": student_class,
        "nationality": nationality
    }
    print(f"payload: {payload}")
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url=Environment.BASE_URL + Environment.UPDATE_END_POINT, json=payload, headers=headers)
    print(f"response: {response.text}")
    return response


def update_student(student: Student):
    return update_student_detail(student.get_id(), student.get_first_name(), student.get_last_name(),
                                 student.get_nationality(),
                                 student.get_student_class())
