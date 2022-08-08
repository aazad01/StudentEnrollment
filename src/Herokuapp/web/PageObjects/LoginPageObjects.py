from selenium.webdriver.common.by import By

from Herokuapp.helper.Browser import *


class LoginPageObjects:
    def header(self):
        return driver.find_element(By.TAG_NAME, 'h2')

    def subheader(self):
        return driver.find_element(By.TAG_NAME, 'h4')

    def username(self):
        return driver.find_element(By.ID, 'username')

    def password(self):
        return driver.find_element(By.ID, 'password')

    def submit(self):
        return driver.find_element(By.TAG_NAME, 'button')

    def error(self):
        return driver.find_element(By.ID, 'flash')
