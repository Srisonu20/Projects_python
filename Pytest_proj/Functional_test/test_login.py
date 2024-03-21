import time

import pytest
from _pytest import mark
from selenium.webdriver import ActionChains

from Functional_test.test_google_search import Test_google_search
from PageObject.login_page_with_mousehover import Test_sign_up


@pytest.mark.fixture("TestBase")
class Test_login(Test_google_search):

    def test_login_page(self):
        lp = Test_sign_up(self.driver)
        time.sleep(2)

        ActionChains(self.driver).move_to_element(lp.get_hover()).perform()
        time.sleep(2)

        lp.get_my_profile().click()
        time.sleep(2)

        lp.get_enter_num().send_keys("8618943318")
        time.sleep(2)

        lp.get_req_otp().click()
        time.sleep(2)

        lp.get_verify().click()
        time.sleep(2)





