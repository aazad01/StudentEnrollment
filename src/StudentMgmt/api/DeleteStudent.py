import requests

import Environment


def delete_student(id: int):
    param = {
        "id": id
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.delete(url=Environment.BASE_URL + Environment.DELETE_END_POINT, json=param, headers=headers)
    r = response
    print(r)
    return response
