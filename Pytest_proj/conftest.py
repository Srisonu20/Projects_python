import time

import pytest
from selenium import webdriver

@pytest.fixture(scope = "class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.implicitly_wait(30)
    driver.maximize_window()
    time.sleep(2)
    request.cls.driver = driver
    yield
    driver.close()
