# Тесты для проверки получения списка заказов через API
import requests
import allure
import pytest
from api_urls import MAIN_URL, GET_ORDER_LIST_URL

class TestOrderList:

    @allure.title('Проверка, что в тело ответа возвращается список заказов')
    @allure.description("Проверяет, что API возвращает список заказов в теле ответа при успешном запросе")
    @pytest.mark.parametrize("params", [{"nearestStation": '["1", "2"]'}, {}], ids=["with_station", "without_station"])
    def test_returns_order_list(self, params):
        response = requests.get(f'{MAIN_URL}{GET_ORDER_LIST_URL}', params=params)
        assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
        response_body = response.json()['orders']
        assert isinstance(response_body, list), "В ответе ожидался список заказов"