import requests
import json
import datetime, time

from StudentMgmt import Environment

END_POINT = "deleteStudent"

def delete_student(id: int):
    param = {
        "id": id
    }

    response = requests.delete(url=Environment.BASE_URL + END_POINT, params=param)
    r = response.json()
    print(r)