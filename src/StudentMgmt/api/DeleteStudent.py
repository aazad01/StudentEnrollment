import requests

import environment


def delete_student(id: int):
    param = {
        "id": id
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.delete(url=environment.BASE_URL + environment.DELETE_END_POINT, json=param, headers=headers)
    r = response
    print(r)
    return response
