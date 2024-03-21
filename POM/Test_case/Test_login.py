import time

import pytest
from selenium.webdriver.chrome import webdriver

from Page_objects.Dashboard_page import Dashboard
from Page_objects.Login_Page import Login


@pytest.mark.usefixtures("setup")
class Testlogin:


    @pytest.mark.parametrize("username,password,condition",[("Admin","admin123",'+'),("Amin","admin123",'+'),("Admin","admin123",'+')])
    def test_001(self,setup,username,password,condition):
        lg = Login(self)
        time.sleep(5)
        db = Dashboard(self)
        time.sleep(5)
        lg.input_username(username)
        time.sleep(5)
        lg.input_password(password)
        time.sleep(5)
        lg.click_login()
        time.sleep(5)
        if condition == '+':
            if 'Welcome' in db.welcome_msg():
                assert True

            else:
                assert False

        elif condition == '-':
            if "Invalid credentials" in lg.invalid_msg():
                assert True

            else:
                assert False
