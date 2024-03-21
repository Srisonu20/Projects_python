import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)


        self.textbox_username_xpath = (By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]")
        self.textbox_password_xpath = (By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]")
        self.button_login_xpath = (By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]")
        self.text_invalidmsg_xpath = (By.XPATH,"//span[@id='spanMessage']")




    def input_username(self,username):
        username_element = self.wait.until(EC.presence_of_element_located(self.textbox_username_xpath))
        # self.driver.find_element(*self.textbox_username_xpath).send_keys(username)
        # time.sleep(3)
        username_element.send_keys(username)

    def input_password(self,password):
        password_element = self.wait.until(EC.presence_of_element_located(self.textbox_password_xpath))
        password_element.send_keys(password)
        # self.driver.find_element(*self.textbox_password_xpath).send_keys(password)
        # time.sleep(3)

    def click_login(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self.button_login_xpath))
        login_button.click()
        # self.driver.find_element(*self.button_login_xpath).click()
        # time.sleep(3)

    def invalid_msg(self):
        return self.driver.find_element(*self.text_invalidmsg_xpath).text
        # time.sleep(3)