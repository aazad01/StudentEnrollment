from faker import Faker

from helper import Randoms


class Student:

    def __init__(self):
        fake = Faker()
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.nationality = fake.country()
        self.id = None
        self.student_class = Randoms.random_string(10)

    def set_first_name(self, value):
        self.first_name = value
        return self

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, value):
        self.last_name = value
        return self

    def get_last_name(self):
        return self.last_name

    def set_nationality(self, value):
        self.nationality = value
        return self

    def get_nationality(self):
        return self.nationality

    def set_id(self, value):
        self.id = value
        return self

    def get_id(self):
        return self.id

    def set_student_class(self, value):
        self.student_class = value
        return self

    def get_student_class(self):
        return self.student_class
