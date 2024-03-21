from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from Utility.TestBase import TestBase

"""  ActionChains Mouse hover is used   """
class Test_sign_up(TestBase):
    def __init__(self,driver):
        self.driver = driver
        self.hover = (By.XPATH,"//a[contains(text(),'Login')]")
        self.my_profile = (By.XPATH,"//body/div[@id='container']/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/ul[1]/li[1]")
        self.enter_num = (By.XPATH,"//body/div[@id='container']/div[1]/div[3]/div[1]/div[2]/div[1]/form[1]/div[1]/input[1]")
        # self.submit = (By.XPATH,"//body/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/button[1]")
        self.req_otp = (By.XPATH,"//button[contains(text(),'Request OTP')]")
        self.verify = (By.XPATH,"//button[contains(text(),'Verify')]")

    def get_hover(self):
        return self.driver.find_element(*self.hover)

    def get_my_profile(self):
        return self.driver.find_element(*self.my_profile)

    def get_enter_num(self):
        return self.driver.find_element(*self.enter_num)

    # def get_submit(self):
    #     return self.driver.find_element(*self.submit)

    def get_req_otp(self):
        return self.driver.find_element(*self.req_otp)

    def get_verify(self):
        return self.driver.find_element(*self.verify)



    # # def test_sign_up_hover(self):
    #     action = ActionChains(driver)
    #     action.move_to_element( self.driver.find_element(By.XPATH,"//a[contains(text(),'Login')]")).perform()
    #     sing_up_btn =self.driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]")
    #     sing_up_btn.click()
    #     enter_num = self.driver.find_element(By.CLASS_NAME,"//body/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/input[1]")
    #     enter_num.send_keys("8618943318")
    #
    #
    #     req_otp = self.driver.find_element(By.CLASS_NAME,"_2KpZ6l _2HKlqd _3AWRsL")
    #     req_otp.clicl()
    #     verify = self.driver.find_element(By.XPATH,"_2KpZ6l _14EHzR _3dESVI")
    #     verify.click()