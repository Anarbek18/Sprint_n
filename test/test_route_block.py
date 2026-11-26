import allure

import data


@allure.feature("Отрисовка блока с выбором маршрута")
class TestRouteBlock:

    @allure.title("Для двух разных адресов отображается блок с выбором маршрута")
    def test_route_block_displayed_for_different_addresses(self, different_addresses_route, route_page):
        assert route_page.is_route_block_displayed()

    @allure.title("Для одинаковых адресов блок маршрута содержит текст о бесплатной поездке")
    def test_route_block_text_for_same_addresses(self, same_addresses_route, route_page):
        assert route_page.get_route_info_text() == data.SAME_ADDRESS_ROUTE_TEXT
