from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = None


def wait_for(element):
    return WebDriverWait(driver, 100).until(EC.presence_of_element_located(element))
