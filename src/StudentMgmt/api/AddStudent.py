import requests

from StudentMgmt import Environment, Student


class AddStudent:
    def add_student_detail(self, id, first_name, last_name, nationality, student_class):
        payload = {
            "firstName": first_name,
            "id": id,
            "last_name": last_name,
            "nationality": nationality,
            "studentClass": student_class
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Environment.BASE_URL + Environment.ADD_END_POINT, json=payload, headers=headers)
        r = response
        print(r.text)
        return r

    def add_student(self, student: Student):
        return self.add_student_detail(student.get_id(), student.get_first_name(), student.get_last_name(),
                                       student.get_nationality(),
                                       "K001")
