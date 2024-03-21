import pytest


@pytest.mark.usefixtures("setup")
class TestBase:
    def testbase(self):
        pass
