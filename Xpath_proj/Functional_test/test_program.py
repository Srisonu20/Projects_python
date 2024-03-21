import time

import pytest

from Functional_test.test_home_page import Test_home_page
from Page_object.program import Program
from Utility.TestBase import TestBase


@pytest.mark.fixture("TestBase")
class Test_programs(Test_home_page):
    def test_python_programs(self,TestBase):

        py_prog = Program(TestBase.driver)
        time.sleep(3)


        py_prog.get_scroll()
        time.sleep(3)
