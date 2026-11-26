from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    MAP = (By.CSS_SELECTOR, "#map")
    MAP_ROUTE_POINTS = (By.CSS_SELECTOR, "#map ymaps[class*='placemark']")

    def open(self, url):
        self.driver.get(url)

    def set_from(self, address):
        self.type_text(self.FROM_INPUT, address)

    def set_to(self, address):
        self.type_text(self.TO_INPUT, address)

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def is_map_displayed(self):
        return self.is_displayed(self.MAP)

    def get_route_points_count(self):
        return self.count(self.MAP_ROUTE_POINTS)
