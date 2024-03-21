# import time
#
# import pytest
# from selenium.webdriver import ActionChains
#
# from Functional_test.test_google_search import Test_google_search
# from PageObject.scrolling import Scroll
# from Utility.TestBase import TestBase
#
# @pytest.mark.fixture("TestBase")
# class Scroll(Test_google_search):
#     def test_scrolling(self):
#
#
#         scroll_ud = Scroll(self.driver)
#
#         time.sleep(2)
#
#         scroll_ud.get_scroll_down()
#         time.sleep(2)
#
#         scroll_ud.get_scroll_up()
#         time.sleep(2)
#
#         ActionChains(self.driver).context_click(scroll_ud.get_ryt_click()).perform()
#         time.sleep(2)
#
#         scroll_ud.get_screen_shot()
#         time.sleep(2)
#
#         scroll_ud.get_adds()
#         time.sleep(2)
#
#         ActionChains(self.driver).move_to_element(scroll_ud.get_assert_price()).click()
#         # google_s.get_assert_price()
#         time.sleep(2)