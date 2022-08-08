import requests

from StudentMgmt import Environment


def update_student(id: int, first_name: str, last_name: str, nationality: str, student_class: str):
    payload = {
        "firstName": first_name,
        "id": id,
        "last_name": last_name,
        "nationality": nationality,
        "studentClass": student_class
    }

    response = requests.put(url=Environment.BASE_URL + Environment.UPDATE_END_POINT, params=payload)
    r = response.json()
    print(r)
