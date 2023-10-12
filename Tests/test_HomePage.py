import time

from Pages.HomePage import HomePage
from Tests.test_BasePage import BaseTest
import pytest

class Test_Home(BaseTest):
    def test_make_my_trip(self):
        self.page = HomePage(self.driver)
        self.page.close_login()
        self.page.close_popup()
        self.page.switch()

        self.page.flights()
        time.sleep(5)
        self.page.popup_close()

        self.page.trains()
        # time.sleep(0)

        self.page.teardown()

