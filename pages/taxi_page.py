import re

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TaxiPage(BasePage):
    TARIFFS = (By.CSS_SELECTOR, ".tcard")
    ACTIVE_TARIFF = (By.CSS_SELECTOR, ".tcard.active")
    ACTIVE_TARIFF_PRICE = (By.CSS_SELECTOR, ".tcard.active .tcard-price")
    TARIFF_BY_NAME = "//div[contains(@class,'tcard')][.//div[@class='tcard-title'][text()='{}']]"
    TARIFF_INFO_BUTTON = TARIFF_BY_NAME + "//button[contains(@class,'tcard-i')]"
    TARIFF_DESCRIPTION = TARIFF_BY_NAME + "//div[@class='i-dPrefix']"

    PHONE_FIELD = (By.XPATH, "//div[contains(@class,'np-text')][text()='Телефон']")
    PAYMENT_FIELD = (By.CSS_SELECTOR, ".pp-button .pp-text")
    COMMENT_FIELD = (By.XPATH, "//*[contains(text(),'Комментарий водителю')]")
    REQUIREMENTS_FIELD = (By.CSS_SELECTOR, ".reqs .reqs-head")
    OPTION_SWITCH = "//div[@class='r-sw-label'][text()='{}']/following::span[contains(@class,'slider')][1]"
    OPTION_CHECKBOX = "//div[@class='r-sw-label'][text()='{}']/following::input[contains(@class,'switch-input')][1]"
    ORDER_BUTTON = (By.XPATH, "//*[contains(text(),'Ввести номер и заказать')]")

    ORDER_WINDOW = (By.CSS_SELECTOR, ".order .order-body")
    ORDER_TITLE = (By.CSS_SELECTOR, ".order .order-header-title")
    ORDER_TIMER = (By.CSS_SELECTOR, ".order .order-header-content .timer")
    CAR_NUMBER = (By.CSS_SELECTOR, ".order-number .number")
    TARIFF_IMAGE = (By.CSS_SELECTOR, ".order-number img")
    DRIVER_NAME = (By.CSS_SELECTOR, ".order-btn-group:first-child > div:not(.order-button)")
    DRIVER_PHOTO = (By.CSS_SELECTOR, ".order-btn-group:first-child .order-button img")
    DRIVER_RATING = (By.CSS_SELECTOR, ".order-btn-rating")
    CANCEL_BUTTON = (By.XPATH, "//div[@class='order-btn-group'][div[text()='Отменить']]//button")
    DETAILS_BUTTON = (By.XPATH, "//div[@class='order-btn-group'][div[text()='Детали']]//button")
    DETAILS_COST = (By.XPATH, "//div[text()='Еще про поездку']/following-sibling::div[@class='o-d-sh']")

    ORDER_DONE_TIMEOUT = 60

    @staticmethod
    def _digits(text):
        return re.sub(r"\D", "", text)

    def get_tariffs_count(self):
        return self.count(self.TARIFFS)

    def is_active_tariff_displayed(self):
        return self.is_displayed(self.ACTIVE_TARIFF)

    def select_tariff(self, name):
        self.click((By.XPATH, self.TARIFF_BY_NAME.format(name)))

    def get_active_tariff_price(self):
        return self._digits(self.get_text(self.ACTIVE_TARIFF_PRICE))

    def hover_tariff_info(self, name):
        self.hover((By.XPATH, self.TARIFF_INFO_BUTTON.format(name)))

    def get_tariff_description(self, name):
        return self.get_text((By.XPATH, self.TARIFF_DESCRIPTION.format(name)))

    def is_phone_field_displayed(self):
        return self.is_displayed(self.PHONE_FIELD)

    def is_payment_field_displayed(self):
        return self.is_displayed(self.PAYMENT_FIELD)

    def is_comment_field_displayed(self):
        return self.is_displayed(self.COMMENT_FIELD)

    def is_requirements_field_displayed(self):
        return self.is_displayed(self.REQUIREMENTS_FIELD)

    def enable_option(self, name):
        self.click((By.XPATH, self.OPTION_SWITCH.format(name)))

    def is_option_enabled(self, name):
        return self.is_selected((By.XPATH, self.OPTION_CHECKBOX.format(name)))

    def click_order(self):
        self.click(self.ORDER_BUTTON)

    def get_order_title(self):
        return self.get_text(self.ORDER_TITLE)

    def is_timer_displayed(self):
        return self.is_displayed(self.ORDER_TIMER)

    def is_cancel_button_displayed(self):
        return self.is_displayed(self.CANCEL_BUTTON)

    def is_details_button_displayed(self):
        return self.is_displayed(self.DETAILS_BUTTON)

    def wait_for_order_done(self):
        self.find(self.CAR_NUMBER, self.ORDER_DONE_TIMEOUT)

    def is_car_number_displayed(self):
        return self.is_displayed(self.CAR_NUMBER)

    def is_tariff_image_displayed(self):
        return self.is_displayed(self.TARIFF_IMAGE)

    def is_driver_name_displayed(self):
        return self.is_displayed(self.DRIVER_NAME)

    def is_driver_photo_displayed(self):
        return self.is_displayed(self.DRIVER_PHOTO)

    def is_driver_rating_displayed(self):
        return self.is_displayed(self.DRIVER_RATING)

    def click_details(self):
        self.click(self.DETAILS_BUTTON)

    def get_details_price(self):
        return self._digits(self.get_text(self.DETAILS_COST))

    def click_cancel(self):
        self.click(self.CANCEL_BUTTON)

    def is_order_window_closed(self):
        return self.is_invisible(self.ORDER_WINDOW)
