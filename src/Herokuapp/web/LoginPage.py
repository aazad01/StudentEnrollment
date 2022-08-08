from Herokuapp.helper.Browser import *
from Herokuapp.web.PageObjects.LoginPageObjects import LoginPageObjects


class LoginPage(LoginPageObjects):

    def page_load(self):
        wait_for(self.header())
        wait_for(self.subheader())
        wait_for(self.username())
        wait_for(self.password())
        wait_for(self.submit())

    def get_header(self):
        return wait_for(self.header()).text

    def get_subheader(self):
        return wait_for(self.subheader()).text

    def enter_username(self, value):
        wait_for(self.username()).send_keys(value)

    def enter_password(self, value):
        wait_for(self.password()).send_keys(value)

    def click_submit(self):
        wait_for(self.submit()).click()

    def get_alert(self):
        return wait_for(self.error()).text
