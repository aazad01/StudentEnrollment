import requests

from StudentMgmt import Environment


def fetch_student(id: int, student_class: str):
    params = {
        "id": id,
        "studentClass": student_class
    }
    response = requests.get(url=Environment.BASE_URL + Environment.FETCH_END_POINT, params=params)
    r = response.json()
    print(r)
    return response
