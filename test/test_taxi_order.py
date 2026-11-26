import allure
import pytest

import data


@allure.feature("Заказ тарифа Такси")
class TestTaxiOrderForm:

    @allure.title("Форма заказа содержит все тарифы по ТЗ")
    def test_order_form_has_all_tariffs(self, taxi_order_form):
        assert taxi_order_form.get_tariffs_count() == data.TARIFFS_COUNT

    @allure.title("В форме заказа один из тарифов активный")
    def test_order_form_has_active_tariff(self, taxi_order_form):
        assert taxi_order_form.is_active_tariff_displayed()

    @allure.title("Описание тарифа во всплывающем окне соответствует ТЗ")
    @pytest.mark.parametrize("tariff_name, description", data.TARIFF_DESCRIPTIONS.items())
    def test_tariff_popup_description(self, taxi_order_form, tariff_name, description):
        taxi_order_form.hover_tariff_info(tariff_name)
        assert taxi_order_form.get_tariff_description(tariff_name) == description

    @allure.title("Под тарифами отображается поле Телефон")
    def test_phone_field_displayed(self, taxi_order_form):
        assert taxi_order_form.is_phone_field_displayed()

    @allure.title("Под тарифами отображается поле Способ оплаты")
    def test_payment_field_displayed(self, taxi_order_form):
        assert taxi_order_form.is_payment_field_displayed()

    @allure.title("Под тарифами отображается поле Комментарий водителю")
    def test_comment_field_displayed(self, taxi_order_form):
        assert taxi_order_form.is_comment_field_displayed()

    @allure.title("Под тарифами отображается поле Требования к заказу")
    def test_requirements_field_displayed(self, taxi_order_form):
        assert taxi_order_form.is_requirements_field_displayed()


@allure.feature("Заказ тарифа Такси: полный флоу")
class TestTaxiOrderFlow:

    @allure.title("Чекбокс Столик для ноутбука включается")
    def test_laptop_table_option_enabled(self, taxi_order_form):
        taxi_order_form.select_tariff(data.TARIFF_WORK)
        taxi_order_form.enable_option(data.OPTION_LAPTOP_TABLE)
        assert taxi_order_form.is_option_enabled(data.OPTION_LAPTOP_TABLE)

    @allure.title("В окне ожидания машины отображается заголовок Поиск машины")
    def test_search_window_title(self, searching_car_window):
        assert searching_car_window.get_order_title() == data.SEARCH_WINDOW_TITLE

    @allure.title("В окне ожидания машины отображается таймер")
    def test_search_window_timer_displayed(self, searching_car_window):
        assert searching_car_window.is_timer_displayed()

    @allure.title("В окне ожидания машины отображается кнопка Отменить")
    def test_search_window_cancel_button_displayed(self, searching_car_window):
        assert searching_car_window.is_cancel_button_displayed()

    @allure.title("В окне ожидания машины отображается кнопка Детали")
    def test_search_window_details_button_displayed(self, searching_car_window):
        assert searching_car_window.is_details_button_displayed()

    @allure.title("В окне совершенного заказа отображается номер автомобиля")
    def test_done_window_car_number(self, car_found_window):
        assert car_found_window.is_car_number_displayed()

    @allure.title("В окне совершенного заказа отображается картинка тарифа")
    def test_done_window_tariff_image(self, car_found_window):
        assert car_found_window.is_tariff_image_displayed()

    @allure.title("В окне совершенного заказа отображается имя водителя")
    def test_done_window_driver_name(self, car_found_window):
        assert car_found_window.is_driver_name_displayed()

    @allure.title("В окне совершенного заказа отображается фото водителя")
    def test_done_window_driver_photo(self, car_found_window):
        assert car_found_window.is_driver_photo_displayed()

    @allure.title("В окне совершенного заказа отображается рейтинг водителя")
    def test_done_window_driver_rating(self, car_found_window):
        assert car_found_window.is_driver_rating_displayed()

    @allure.title("В окне совершенного заказа отображается кнопка Отменить")
    def test_done_window_cancel_button(self, car_found_window):
        assert car_found_window.is_cancel_button_displayed()

    @allure.title("В окне совершенного заказа отображается кнопка Детали")
    def test_done_window_details_button(self, car_found_window):
        assert car_found_window.is_details_button_displayed()

    @allure.title("В окне Детали указана стоимость, выбранная при выборе тарифа")
    def test_details_cost_matches_tariff_cost(self, taxi_order_form):
        taxi_order_form.select_tariff(data.TARIFF_WORK)
        tariff_price = taxi_order_form.get_active_tariff_price()
        taxi_order_form.enable_option(data.OPTION_LAPTOP_TABLE)
        taxi_order_form.click_order()
        taxi_order_form.wait_for_order_done()
        taxi_order_form.click_details()
        assert taxi_order_form.get_details_price() == tariff_price

    @allure.title("После нажатия Отмена окно заказа закрывается")
    def test_cancel_closes_order_window(self, car_found_window):
        car_found_window.click_cancel()
        assert car_found_window.is_order_window_closed()
