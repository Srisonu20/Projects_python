import time
from lib2to3.pgen2 import driver

from selenium.common import InvalidArgumentException, NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from telnetlib3 import EC
from selenium.webdriver.support import expected_conditions as EC


from Utility.TestBase import TestBase
from selenium.webdriver.common.keys import Keys

""" Scrolling Up and Down , Right_click , Screenshot , navigate_back """
class Scroll(TestBase):
    def __init__(self, driver):
        self.driver = driver

        self.scroll_down =  ActionChains(self.driver).key_up(Keys.SPACE).key_down(Keys.SPACE).perform()
        time.sleep(2)
        self.scroll_up = ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.SPACE).key_up(Keys.SPACE).key_up(Keys.SHIFT).perform()
        time.sleep(2)

        self.ryt_click = (By.XPATH,"//div[contains(text(),'APPLE iPhone 15 Pro Max (Natural Titanium, 256 GB)')]")

        self.assert_price = (By.XPATH,
                             "//body/div[@id='container']/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/a[1]/div[2]/div[2]/div[1]/div[1]/div[1]")

        self.screen_shot = driver.save_screenshot("C:\SPython_Proj\Pytest_proj\Screen_shot\image.png")

        self.adds = (By.XPATH,"//body/div[@id='container']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/a[1]/div[1]/img[1]")
        print("total adds : ",len(self.adds))


        self.handle_login = (By.XPATH, "//span[contains(text(),'✕')]")


    def get_scroll_down(self):
        while True:
            try:
                self.driver.find_element(self.scroll_down)
                time.sleep(0.5)
            except InvalidArgumentException:
                break

    def get_scroll_up(self):
        while True:
            try:
                self.driver.find_element(self.scroll_up)
                time.sleep(0.5)
            except InvalidArgumentException:
                break

    def get_ryt_click(self):
        return self.driver.find_element(*self.ryt_click)

    def get_screen_shot(self):
        return self.screen_shot

    def get_assert_price(self):
        try:
            x = self.assert_price
            y = WebDriverWait(driver, 5).until(EC.presence_of_element_located(x))
            assert y is not None, " element is present "

        except Exception as e:
            assert False, " element is not presence"
            print("continue")

        finally:
            print("Continue....")

    def get_adds(self):
        self.driver.back()
        return self.driver.find_element(*self.adds)

    def get_handle_login(self):
        try:
            handle = self.handle_login
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(handle))
            login_ele = self.driver.find_element(*self.handle_login)
            if login_ele.is_displayed():
                login_ele.click()
                print("not found")
            else:
                print("login element not found")

        except (TimeoutException,NoSuchElementException) as e:
            print(f"Login pop-up not found within the specified time. ERROR: {e}")












