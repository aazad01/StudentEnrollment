import requests

import environment


def fetch_student(id: int, student_class: str):
    params = {
        "id": id,
        "studentClass": student_class
    }
    response = requests.get(url=environment.BASE_URL + environment.FETCH_END_POINT, params=params)
    r = response.json()
    print(r)
    return response
