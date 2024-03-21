import time
from lib2to3.pgen2 import driver
from telnetlib import EC

import pytest
from telnetlib3 import EC

from selenium.common import TimeoutException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Utility.TestBase import TestBase


class Home_page(TestBase):
    def __init__(self,driver):
        self.driver = driver
        # """
        # XPATH is Used combination of //tagname[@attribute='vale']  //tagname[text() = 'value'] (parent and child tags)
        # """
        self.header_python = (By.XPATH,"//div[@class='header-main__slider']//a[text()='Python']")

        self.close_popup = (By.XPATH,"// button[ @ id = 'three90__modal-close-btn']")

        # # // button[ @ id = 'three90__modal-close-btn']
        # # """
        # XPATH is Used combination of (parent tagname) //tagname[@attribute='vale'] and [position = number]'
        # """

        self.header_in_python = (By.XPATH,"(//div[@class='header-main__slider']//a)[position() = 13]")


    def get_home(self):
        return self.driver.find_element(*self.header_python)




    def get_popup(self):
        # return self.driver.switch_to.alert().accept()


        x = self.driver.find_element(*self.close_popup)
        y = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(x))
        return y
        # except NoSuchElementException as e:
        #     print("continue")


    def get_python_pro(self):

        return self.driver.find_element(*self.header_in_python)





