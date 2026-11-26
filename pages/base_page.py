from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    def _wait(self, timeout=None):
        return WebDriverWait(self.driver, timeout or self.DEFAULT_TIMEOUT)

    def find(self, locator, timeout=None):
        return self._wait(timeout).until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        self._wait().until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self._wait().until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=None):
        return self.find(locator, timeout).text

    def is_displayed(self, locator):
        return self.find(locator).is_displayed()

    def is_enabled(self, locator):
        return self.find(locator).is_enabled()

    def is_selected(self, locator):
        return self._wait().until(EC.presence_of_element_located(locator)).is_selected()

    def is_invisible(self, locator):
        return self._wait().until(EC.invisibility_of_element_located(locator))

    def hover(self, locator):
        element = self.find(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def count(self, locator):
        return len(self.find_all(locator))

    def get_texts(self, locator):
        return [element.text for element in self.find_all(locator)]
