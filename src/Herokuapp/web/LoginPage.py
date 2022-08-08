from Herokuapp.helper.Browser import *
from Herokuapp.web.PageObjects.LoginPageObjects import LoginPageObjects


class LoginPage(LoginPageObjects):

    def check_page(self):
        wait_for(self.header())
        wait_for(self.subheader())
        wait_for(self.username())
        wait_for(self.password())
        wait_for(self.submit())

    def enter_username(self, value):
        wait_for(self.username())
        self.username().send_keys(value)

    def enter_password(self, value):
        wait_for(self.password())
        self.password().send_keys(value)

    def click_submit(self):
        wait_for(self.submit())
        self.submit().click()

    def check_errors(self, value):
        wait_for(self.error())
        error = self.error()
        assert error.is_displayed()
        assert error.text == value
