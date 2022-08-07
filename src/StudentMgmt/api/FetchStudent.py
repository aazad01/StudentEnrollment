import requests
import json
import datetime, time

from StudentMgmt import Environment

END_POINT = "fetchStudent"

def add_student(id: int, student_class: str):
    params = {
        "id": id,
        "studentClass": student_class
    }
    response = requests.get(url=Environment.BASE_URL + END_POINT, params=params)
    r = response.json()
    print(r)