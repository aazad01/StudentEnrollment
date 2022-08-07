import requests
import json
import datetime, time

END_POINT = "addStudent"

def add_student(id: int, first_name: str, last_name: str, nationality: str, student_class: str):
    payload = {
        "firstName": first_name,
        "id": id,
        "last_name": last_name,
        "nationality": nationality,
        "studentClass": student_class
    }

    request = requests.post(Environment.base_url + END_POINT)
