import time
# from lib2to3.pgen2 import driver
from telnetlib3 import EC
from webdriver_manager.core import driver
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Utility.TestBase import TestBase

"""  Send_keys and Click methods are used
                     AND Dynamic DropDown """


class Google_search(TestBase):

    def __init__(self, driver):
        self.driver = driver
        self.search = (By.ID,"APjFqb")
        self.btn = (By.XPATH, "//body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        self.select_first_link = (By.XPATH,"//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]/div[1]/div[1]/div[1]/cite[1]")

        self.search_bar = (By.XPATH,"//header/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")
        self.first_option = (By.XPATH,"(//form[contains(@class,'_2rslOn header-form-search OpXDaO')]//a)[1]")




    def get_search(self):
        return self.driver.find_element(*self.search)

    def get_btn(self):
        return self.driver.find_element(*self.btn)

    def get_first_link(self):
        return self.driver.find_element(*self.select_first_link)




    def get_search_bar(self):
        return self.driver.find_element(*self.search_bar)

    def get_first_option(self):
        return self.driver.find_element(*self.first_option)















