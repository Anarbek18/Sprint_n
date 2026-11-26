import pytest
from selenium import webdriver

import data
from pages.main_page import MainPage
from pages.route_page import RoutePage
from pages.taxi_page import TaxiPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open(data.URL)
    return page


@pytest.fixture
def route_page(driver):
    return RoutePage(driver)


@pytest.fixture
def taxi_page(driver):
    return TaxiPage(driver)


@pytest.fixture
def different_addresses_route(main_page):
    main_page.set_route(data.ADDRESS_A, data.ADDRESS_B)
    return main_page


@pytest.fixture
def same_addresses_route(main_page):
    main_page.set_route(data.ADDRESS_A, data.ADDRESS_A)
    return main_page


@pytest.fixture
def fast_route(different_addresses_route, route_page):
    route_page.select_fast()
    return route_page


@pytest.fixture
def taxi_order_form(fast_route, taxi_page):
    fast_route.click_call_taxi()
    return taxi_page


@pytest.fixture
def searching_car_window(taxi_order_form):
    taxi_order_form.select_tariff(data.TARIFF_WORK)
    taxi_order_form.enable_option(data.OPTION_LAPTOP_TABLE)
    taxi_order_form.click_order()
    return taxi_order_form


@pytest.fixture
def car_found_window(searching_car_window):
    searching_car_window.wait_for_order_done()
    return searching_car_window
