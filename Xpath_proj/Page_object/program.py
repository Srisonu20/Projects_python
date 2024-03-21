from selenium.webdriver.common.by import By

from Utility.TestBase import TestBase


class Program(TestBase):
    def __init__(self,driver):
        self.driver = driver

        self.scroll = driver.execute_script("window.scrollBy(0,500)","")




    def get_scroll(self):
        return self.scroll

