import time

import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_BasePage import BaseTest


class Test_Login(BaseTest):

    # def test_login_page_title(self):
    #     print("Test Login Title")
    #     self.loginPage = LoginPage(self.driver)
    #     title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
    #     assert title == TestData.LOGIN_PAGE_TITLE

    # def test_login(self):
    #     self.loginPage = LoginPage(self.driver)
    #     self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
    def tests(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.close_login()
        time.sleep(5)
        self.loginPage.choose_roundTrip()
        self.loginPage.close_popup()

