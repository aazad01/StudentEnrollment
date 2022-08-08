from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()


def wait_for(element):
    WebDriverWait(driver, 100).until(lambda driver: element)
