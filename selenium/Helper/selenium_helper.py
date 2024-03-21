from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Logs import logs_file

log = logs_file.get_logs()


class SeleniumHelper:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, page_url):
        log.info(f"Opening page: {page_url}")
        self.driver.get(page_url)

    def insert_text_in_input_field(self, locator, input_text):
        log.info(f"Entering text: {input_text} in locator: {list(locator.values())[0]}")
        self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).send_keys(input_text)

    def user_selects_the_first_link(self, locator):
        log.info(f"Clicking on: {list(locator.values())[0]}")
        self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).click()


    def user_navigates_to_the_menu(self, locator):
        log.info(f"Clicking on: {list(locator.values())[0]}")
        self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).click()







