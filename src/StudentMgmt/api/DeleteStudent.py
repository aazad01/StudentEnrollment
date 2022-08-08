import requests

from StudentMgmt import Environment


def delete_student(id: int):
    param = {
        "id": id
    }

    response = requests.delete(url=Environment.BASE_URL + Environment.DELETE_END_POINT, params=param)
    r = response.json()
    print(r)
