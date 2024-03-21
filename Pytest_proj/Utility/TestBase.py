import pytest
from selenium.webdriver.support.wait import WebDriverWait
from telnetlib3 import EC


@pytest.mark.usefixtures("setup")
class TestBase:
    pass


