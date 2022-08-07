import requests
import json
import datetime, time

from StudentMgmt import Environment

END_POINT = "addStudent"

def add_student(id: int, first_name: str, last_name: str, nationality: str, student_class: str):
    payload = {
        "firstName": first_name,
        "id": id,
        "last_name": last_name,
        "nationality": nationality,
        "studentClass": student_class
    }

    response = requests.post(Environment.BASE_URL + END_POINT)
    r = response.json()
    print(r)