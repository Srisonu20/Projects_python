from selenium.webdriver.common.by import By

from Utility.TestBase import TestBase

""" SWITCH WINDOW  : Handling multiple window """
class Product(TestBase):

    def __init__(self,driver):
        self.driver = driver
        self.click_on_prod = (By.XPATH,
                         "//div[contains(text(),'APPLE iPhone 15 Pro Max (Natural Titanium, 512 GB)')]")
        self.hover_1st_img = (By.XPATH,
                         "//body/div[@id='container']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/img[1]")
        self.hover_2nd_img = (By.XPATH,
                         "//body/div[@id='container']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/div[1]/img[1]")
        self.hover_3rd_img = (By.XPATH,
                         "//body/div[@id='container']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/div[1]/div[1]/img[1]")
        self.hover_4th_img = (By.XPATH,"//body/div[@id='container']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[4]/div[1]/div[1]/img[1]")

    def get_click_on_prod(self):
        return self.driver.find_element(*self.click_on_prod)


    def get_hover_1st_img(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        print("windo handle index", handles)
        return self.driver.find_element(*self.hover_1st_img)

    def get_hover_2nd_img(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        print("windo handle index", handles)
        return self.driver.find_element(*self.hover_2nd_img)

    def get_hover_3rd_img(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        print("windo handle index", handles)
        return self.driver.find_element(*self.hover_3rd_img)


    def get_hover_4th_img(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        print("windo handle index", handles)
        return self.driver.find_element(*self.hover_4th_img)