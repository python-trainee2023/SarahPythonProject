import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    LOGIN_LINK = (By.XPATH, "p[@data-cy='LoginHeaderText']")
    EMAIL = (By.ID, "username")
    CONTINUE_BUTTON = (By.XPATH, "button[@data-cy='continueBtn']")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "button[@data-cy='login']")
    POPUP_BUTTON=(By.ID,"webklipper-publisher-widget-container-notification-close-div")
    IFRAME=(By.ID,"webklipper-publisher-widget-container-notification-frame")
    CLOSE_LOGIN = (By.CLASS_NAME, "commonModal__close")
    ROUND_TRIP = (By.XPATH, "li[@data-cy='roundTrip']")
    LOGIN_BOX = (By.XPATH, "section[@data-cy='CommonModal_2']")

    def __init__(self, driver):
        super().__int__(driver)
        self.driver.get(TestData.BASE_URL)

    def choose_roundTrip(self):
        self.do_click(self.ROUND_TRIP)

    def close_login(self):
        self.j_click(self.CLOSE_LOGIN)

    def close_popup(self):
        self.i_frame(self.IFRAME)
        self.j_click(self.POPUP_BUTTON)
        self.switch_to_default()


    # def is_enabled(self):
    #     return self.is_visible(self.LOGIN_BOX)
    #
    # def get_title(self, title):
    #     return self.get_title(title)
    #
    # def do_login(self, username, password):
    #     self.do_click(self.LOGIN_LINK)
    #     # WebDriverWait(self.driver, 1000)
    #     self.do_send_keys(self.EMAIL, username)
    #     self.do_click(self.CONTINUE_BUTTON)
    #     self.do_send_keys(self.PASSWORD, password)
    #     self.do_click(self.LOGIN_BUTTON)
