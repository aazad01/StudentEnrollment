from Herokuapp.helper.Browser import *
from Herokuapp.web.PageObjects.SecureAreaObjects import SecureAreaObjects


class SecureArea(SecureAreaObjects):

    def page_load(self):
        wait_for(self.header())
        wait_for(self.subheader())
        wait_for(self.logout())

    def click_logout(self):
        wait_for(self.logout()).click()

    def get_alert(self):
        return wait_for(self.alert()).text

    def get_header(self):
        return wait_for(self.header()).text

    def get_subheader(self):
        return wait_for(self.subheader()).text
