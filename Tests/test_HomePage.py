import time

from Pages.HomePage import HomePage
from Tests.test_BasePage import BaseTest
import pytest

class Test_Home(BaseTest):
    def test_make_my_trip(self):
        self.page = HomePage(self.driver)
        self.page.close_login()
        self.page.close_popup()
        # time.sleep(5)
        self.page.switch()

        self.page.click_search()
        time.sleep(5)
        self.page.popup_close()
        time.sleep(20)
        self.page.booking()
        time.sleep(30)

        self.page.teardown()

