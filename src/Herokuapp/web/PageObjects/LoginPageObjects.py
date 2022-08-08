from selenium.webdriver.common.by import By


class LoginPageObjects:
    def header(self):
        return (By.TAG_NAME, 'h2')

    def subheader(self):
        return (By.TAG_NAME, 'h4')

    def username(self):
        return (By.ID, 'username')

    def password(self):
        return (By.ID, 'password')

    def submit(self):
        return (By.TAG_NAME, 'button')

    def error(self):
        return (By.ID, 'flash')
