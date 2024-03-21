import time

from selenium.webdriver import ActionChains, Keys


from PageObject.google_search import Google_search

from PageObject.scrolling import Scroll

from Utility.TestBase import TestBase


class Test_google_search(TestBase):

    def test_search(self):
        google_s = Google_search(self.driver)
        time.sleep(2)

        google_s.get_search().send_keys("flipkart")
        time.sleep(2)

        google_s.get_btn().click()
        time.sleep(2)

        google_s.get_first_link().click()
        time.sleep(2)




        google_s.get_search_bar().send_keys("iphone 15")
        time.sleep(2)

        google_s.get_first_option().click()
        time.sleep(2)




        scroll_ud = Scroll(self.driver)
        time.sleep(2)

        scroll_ud.get_scroll_down()
        time.sleep(2)

        scroll_ud.get_scroll_up()
        time.sleep(2)

        ActionChains(self.driver).context_click(scroll_ud.get_ryt_click()).perform()
        time.sleep(2)

        ActionChains(self.driver).move_to_element(scroll_ud.get_assert_price()).click()
        time.sleep(2)

        scroll_ud.get_screen_shot()
        time.sleep(2)

        scroll_ud.get_adds()
        time.sleep(2)

        scroll_ud.get_handle_login().click()
        time.sleep(2)





        # try:
        #     wait = WebDriverWait(self.driver,5)
        #     wait.until(EC.element_to_be_clickable(google_s.get_handle_login()))
        #     ele = google_s.get_handle_login().is_displayed()
        #     if ele in google_s:
        #         return google_s.get_handle_login().click()
        #     else:
        #         pass
        # except NoSuchElementException:
        #     print("not found")


        # google_s.get_handle_login().click()
        # time.sleep(2)

        # search = self.driver.find_element(By.ID,value= "APjFqb")
        # search.send_keys("flipkart")
        # time.sleep(2)
        # btn = self.driver.find_element(By.XPATH, value= "//body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        # btn.click()
        # time.sleep(2)
        # select_first_link = self.driver.find_element(By.XPATH,value="//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]/div[1]/div[1]/div[1]/cite[1]")
        # select_first_link.click()
        # time.sleep(3)
        # try:
        #
        #     handle_login = self.driver.find_element(By.XPATH, value="//span[contains(text(),'✕')]").click()
        #     if handle_login.is_displayed():
        #         handle_login.click()
        #         print("Found link")
        #     else:
        #         pass
        #         print("Not Found")
        # except NoSuchElementException:
        #     print("Not found")
        #
        # time.sleep(3)

        # search_bar = self.driver.find_element(By.XPATH, value="//header/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")
        # search_bar.send_keys("iphone 15")
        # time.sleep(3)
        # first_option = self.driver.find_element(By.XPATH,
        #                                         value="(//form[contains(@class,'_2rslOn header-form-search OpXDaO')]//a)[1]").click()
        # time.sleep(3)









