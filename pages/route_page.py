from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RoutePage(BasePage):
    ROUTE_BLOCK = (By.CSS_SELECTOR, ".type-picker")
    ROUTE_INFO = (By.CSS_SELECTOR, ".type-picker")
    TAB_OPTIMAL = (By.XPATH, "//div[contains(@class,'mode')][text()='Оптимальный']")
    TAB_FAST = (By.XPATH, "//div[contains(@class,'mode')][text()='Быстрый']")
    TAB_CUSTOM = (By.XPATH, "//div[contains(@class,'mode')][text()='Свой']")
    ACTIVE_TAB = (By.CSS_SELECTOR, ".modes-container .mode.active")
    ROUTE_COST = (By.CSS_SELECTOR, ".type-picker .cost")
    ROUTE_TIME = (By.CSS_SELECTOR, ".type-picker .time")
    TRANSPORT_TYPES = (By.CSS_SELECTOR, ".types-container .type")
    ENABLED_TRANSPORT_TYPES = (By.CSS_SELECTOR, ".types-container .type:not(.disabled)")
    TRANSPORT_DRIVE = (By.CSS_SELECTOR, ".types-container .type.drive")
    CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(text(),'Вызвать такси')]")
    BOOK_BUTTON = (By.XPATH, "//button[contains(text(),'Забронировать')]")

    def is_route_block_displayed(self):
        return self.is_displayed(self.ROUTE_BLOCK)

    def get_route_info_text(self):
        return self.get_text(self.ROUTE_INFO)

    def select_optimal(self):
        self.click(self.TAB_OPTIMAL)

    def select_fast(self):
        self.click(self.TAB_FAST)

    def select_custom(self):
        self.click(self.TAB_CUSTOM)

    def select_drive(self):
        self.click(self.TRANSPORT_DRIVE)

    def get_active_tab_text(self):
        return self.get_text(self.ACTIVE_TAB)

    def get_cost(self):
        return self.get_text(self.ROUTE_COST)

    def get_time(self):
        return self.get_text(self.ROUTE_TIME)

    def get_transport_types_count(self):
        return self.count(self.TRANSPORT_TYPES)

    def get_enabled_transport_types_count(self):
        return self.count(self.ENABLED_TRANSPORT_TYPES)

    def is_call_taxi_button_enabled(self):
        return self.is_enabled(self.CALL_TAXI_BUTTON)

    def is_book_button_enabled(self):
        return self.is_enabled(self.BOOK_BUTTON)

    def click_call_taxi(self):
        self.click(self.CALL_TAXI_BUTTON)
