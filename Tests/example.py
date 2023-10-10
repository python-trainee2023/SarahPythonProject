import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class BaseTest:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.makemytrip.com/")
        self.driver.maximize_window()

    # def teardown(self):
    #     self.driver.quit()


class TestLoginPage(BaseTest):

    def test_login(self):
        # username = self.driver.find_element(By.ID, 'user-name')
        # username.send_keys("standard_user")
        # password = self.driver.find_element(By.ID, 'password')
        # password.send_keys("secret_sauce")
        time.sleep(15)

        self.driver.find_element(By.CLASS_NAME, 'wewidgeticon we_close').click()
        time.sleep(5)
