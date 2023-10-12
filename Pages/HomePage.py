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

    FROM_CITY = (By.ID, "fromCity")
    FROM_SELECT = (By.ID, "react-autowhatever-1-section-0-item-0")
    TO_CITY = (By.ID, "toCity")
    TO_SELECT = (By.ID, "react-autowhatever-1-section-0-item-1")
    SEARCH2 = (By.XPATH, '//p[@data-cy="RailSearchWidget_342"]//a')
    DEPARTURE = (By.XPATH, "//div[@aria-label='Sat Nov 18 2023']")
    TRAVELLER = (By.XPATH, '//p[@data-cy="travellerText"]')
    ADULTS = (By.XPATH, "//li[@data-cy='adults-4']")
    CHILDREN = (By.XPATH, '//li[@data-cy="children-2"]')
    INFANTS = (By.XPATH, '//li[@data-cy="infants-1"]')
    APPLY = (By.XPATH, '//button[@data-cy="travellerApplyBtn"]')
    TRAIN = (By.XPATH, '//li[@data-cy="menu_Trains"]')
    BUS = (By.XPATH, '//li[@data-cy="menu_Buses"]')
    CLASS = (By.XPATH, '//li[@data-cy="1A"]')

    CARD = (By.ID, 'train_options_18-11-2023_0')
    GO_AHEAD = (By.XPATH, '/html/body/div[4]/div/div/div/div/div[3]')
    PAY = (By.XPATH, '//div[@class="payNowWrapper"]//div//a')

    def __init__(self, driver):
        super().__int__(driver)
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()

    def popup_close(self):
        self.j_click(self.CROSS_POPUP)

    def trains(self):
        self.do_click(self.TRAIN)
        time.sleep(5)
        self.do_click(self.FROM_CITY)
        self.do_click(self.FROM_SELECT)

        self.do_click(self.TO_SELECT)
        self.do_click(self.DEPARTURE)
        self.do_click(self.CLASS)
        self.do_click(self.SEARCH2)
        time.sleep(10)
        self.do_click(self.CARD)
        time.sleep(5)
        # self.do_click(self.GO_AHEAD)
        # time.sleep(10)
        # self.do_click(self.PAY)

    # def bus(self):
    #     self.do_click(self.BUS)
    #     time.sleep(5)

    def flights(self):
        self.do_click(self.FROM_CITY)
        self.do_click(self.FROM_SELECT)

        self.do_click(self.TO_CITY)
        self.do_click(self.TO_SELECT)

        self.do_click(self.DEPARTURE)
        self.do_click(self.TRAVELLER)
        self.do_click(self.ADULTS)
        self.do_click(self.CHILDREN)
        self.do_click(self.INFANTS)
        self.do_click(self.APPLY)
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
