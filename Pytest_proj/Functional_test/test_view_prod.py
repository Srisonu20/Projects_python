import time

import pytest

from Functional_test.test_google_search import Test_google_search
from PageObject.view_prod import Product
from Utility.TestBase import TestBase

@pytest.mark.fixture("TestBase")
class Test_view_prod(Test_google_search):
    def test_view_prod(self):
        view_p = Product(self.driver)
        time.sleep(2)
        view_p.get_click_on_prod().click()
        time.sleep(2)
        view_p.get_hover_1st_img().click()
        time.sleep(2)
        view_p.get_hover_2nd_img().click()
        time.sleep(2)
        view_p.get_hover_3rd_img().click()
        time.sleep(2)
        view_p.get_hover_4th_img().click()
        time.sleep(2)
