import allure


@allure.feature("Отрисовка маршрута")
class TestRouteDrawing:

    @allure.title("Для двух разных адресов на карте отображаются две точки маршрута")
    def test_two_route_points_displayed_on_map(self, different_addresses_route):
        assert different_addresses_route.get_route_points_count() == 2
