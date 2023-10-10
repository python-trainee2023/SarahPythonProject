from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__int__(driver)
        self.driver.get(TestData.BASE_URL)

