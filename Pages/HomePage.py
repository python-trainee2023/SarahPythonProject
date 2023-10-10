import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):
    POPUP_BUTTON = (By.ID, "webklipper-publisher-widget-container-notification-close-div")
    IFRAME = (By.ID, "webklipper-publisher-widget-container-notification-frame")
    CLOSE_LOGIN = (By.CLASS_NAME, "commonModal__close")
    SEARCH = (By.XPATH, "//p[@data-cy='submit']//a")
    CROSS_POPUP = (By.XPATH, "//div[@class='commonOverlay ']//span")
    VIEW_PRICES = (
    By.XPATH, '//*[@id="bookbutton-RKEY:4ad1c9c6-eece-484b-bc05-ae35852aa94d:13_0"]/span[1]')

    def __init__(self, driver):
        super().__int__(driver)
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()

    def booking(self):
        self.j_click(self.VIEW_PRICES)

    def popup_close(self):
        self.j_click(self.CROSS_POPUP)

    def click_search(self):
        self.do_click(self.SEARCH)

    def close_login(self):
        self.j_click(self.CLOSE_LOGIN)

    def teardown(self):
        self.driver.quit()

    def close_popup(self):
        self.i_frame(self.IFRAME)
        self.j_click(self.POPUP_BUTTON)

    def switch(self):
        self.switch_to_default()
