# Тесты для проверки создания курьера через API
import requests
import pytest
import allure
from api_urls import MAIN_URL, CREATE_COURIER_URL
from Sprint_7.api_utils import generate_courier_data, courier_login, delete_courier
from Sprint_7.data import CourierMessages

class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    @allure.description("Проверяет успешное создание курьера с валидными данными, правильный код ответа и структуру ответа.")
    def test_successful_creation(self):
        courier_data = generate_courier_data()
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": courier_data["firstName"]
        }
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)
        print(f"Request: {payload}")
        print(f"Response: {response.status_code}, {response.text}")
        assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}. Ответ: {response.text}"
        assert response.json().get('ok') is True, f"Ожидался ответ с {{'ok': True}}, получен {response.json()}"
        # Очистка: авторизуемся и удаляем курьера
        login_response = courier_login(payload['login'], payload['password'])
        if login_response and login_response.status_code == 200:
            delete_courier(login_response.json()['id'])

    @allure.title('Попытка создания курьера с существующим логином')
    @allure.description("Проверяет, что при попытке создать курьера с логином, который уже используется, возвращается ошибка.")
    def test_duplicate_login_fails(self):
        # Создаём первого курьера
        courier_data_1 = generate_courier_data()
        response_1 = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=courier_data_1)
        assert response_1.status_code == 201, f"Не удалось создать первого курьера: {response_1.text}"
        
        # Пытаемся создать второго курьера с тем же логином
        courier_data_2 = generate_courier_data()
        payload_2 = {
            "login": courier_data_1["login"],
            "password": courier_data_2["password"],
            "firstName": courier_data_2["firstName"]
        }
        response_courier_2 = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload_2)
        print(f"Request: {payload_2}")
        print(f"Response: {response_courier_2.status_code}, {response_courier_2.text}")
        assert response_courier_2.status_code == 409, f"Ожидался код 409, получен {response_courier_2.status_code}. Ответ: {response_courier_2.text}"
        assert response_courier_2.json()["message"] == CourierMessages.LOGIN_ALREADY_IN_USE, f"Ожидалось сообщение '{CourierMessages.LOGIN_ALREADY_IN_USE}', получено {response_courier_2.json().get('message')}"
        
        # Очистка
        login_response = courier_login(courier_data_1['login'], courier_data_1['password'])
        if login_response and login_response.status_code == 200:
            delete_courier(login_response.json()['id'])

    @allure.title('Проверка создания курьера без обязательных полей')
    @allure.description("Проверяет, что при попытке создать курьера без обязательных полей (login, password), возвращается ошибка.")
    @pytest.mark.parametrize("missing_field", ["login", "password"], ids=["without_login", "without_password"])
    def test_missing_required_field_fails(self, missing_field):
        courier_data = generate_courier_data()
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": courier_data["firstName"]
        }
        payload.pop(missing_field)
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)
        print(f"Request: {payload}")
        print(f"Response: {response.status_code}, {response.text}")
        assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}. Ответ: {response.text}"
        assert response.json()["message"] == CourierMessages.NOT_ENOUGH_DATA, f"Ожидалось сообщение '{CourierMessages.NOT_ENOUGH_DATA}', получено {response.json().get('message')}"

    @allure.title('Создание курьера без firstName успешно')
    @allure.description("Проверяет, что курьер создаётся успешно, если не указан firstName.")
    def test_missing_firstname_succeeds(self):
        courier_data = generate_courier_data()
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)
        print(f"Request: {payload}")
        print(f"Response: {response.status_code}, {response.text}")
        assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}. Ответ: {response.text}"
        assert response.json().get('ok') is True, f"Ожидался ответ с {{'ok': True}}, получен {response.json()}"
        # Очистка
        login_response = courier_login(payload['login'], payload['password'])
        if login_response and login_response.status_code == 200:
            delete_courier(login_response.json()['id'])