import allure

import data


@allure.feature("Подготовка к заказу такси")
class TestTaxiPreparation:

    @allure.title("Переключение Оптимальный -> Быстрый меняет активный таб")
    def test_switch_to_fast_changes_active_tab(self, different_addresses_route, route_page):
        route_page.select_fast()
        assert route_page.get_active_tab_text() == data.TAB_FAST_NAME

    @allure.title("Переключение Оптимальный -> Быстрый пересчитывает время и стоимость")
    def test_switch_to_fast_recalculates_time_and_cost(self, different_addresses_route, route_page):
        time_before = route_page.get_time()
        cost_before = route_page.get_cost()
        route_page.select_fast()
        assert (route_page.get_time(), route_page.get_cost()) != (time_before, cost_before)

    @allure.title("Переключение Быстрый -> Оптимальный меняет активный таб")
    def test_switch_to_optimal_changes_active_tab(self, fast_route):
        fast_route.select_optimal()
        assert fast_route.get_active_tab_text() == data.TAB_OPTIMAL_NAME

    @allure.title("Переключение Быстрый -> Оптимальный пересчитывает время и стоимость")
    def test_switch_to_optimal_recalculates_time_and_cost(self, fast_route):
        time_before = fast_route.get_time()
        cost_before = fast_route.get_cost()
        fast_route.select_optimal()
        assert (fast_route.get_time(), fast_route.get_cost()) != (time_before, cost_before)

    @allure.title("Переключение на вид Свой меняет активный таб")
    def test_switch_to_custom_changes_active_tab(self, different_addresses_route, route_page):
        route_page.select_custom()
        assert route_page.get_active_tab_text() == data.TAB_CUSTOM_NAME

    @allure.title("При виде маршрута Свой активны все типы передвижения")
    def test_custom_route_enables_transport_types(self, different_addresses_route, route_page):
        route_page.select_custom()
        assert route_page.get_enabled_transport_types_count() == len(data.TRANSPORT_TYPES)

    @allure.title("При виде маршрута Быстрый активна кнопка Вызвать такси")
    def test_call_taxi_button_enabled_for_fast_route(self, fast_route):
        assert fast_route.is_call_taxi_button_enabled()

    @allure.title("При виде Свой и типе Драйв активна кнопка Забронировать")
    def test_book_button_enabled_for_custom_drive(self, different_addresses_route, route_page):
        route_page.select_custom()
        route_page.select_drive()
        assert route_page.is_book_button_enabled()
