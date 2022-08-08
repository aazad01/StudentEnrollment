from selenium.webdriver.common.by import By


class SecureAreaObjects:

    def alert(self):
        return (By.ID, 'flash')

    def header(self):
        return (By.TAG_NAME, 'h2')

    def subheader(self):
        return (By.TAG_NAME, 'h4')

    def logout(self):
        return (By.XPATH, ".//a/*[contains(text(),'Logout')]")
