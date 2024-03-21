import time

from selenium.webdriver import ActionChains

from Page_object.home_page import Home_page
from Utility.TestBase import TestBase


class Test_home_page(TestBase):
    def test_home(self):
        home_p = Home_page(self.driver)
        time.sleep(3)

        home_p.get_home().click()
        time.sleep(4)


        home_p.get_popup().click()
        time.sleep(3)

        home_p.get_python_pro().click()
        time.sleep(3)


