# Тесты для проверки авторизации курьера через API
import requests
import pytest
import allure
from api_urls import MAIN_URL, LOGIN_COURIER_URL
from Sprint_7.data import CourierMessages
from Sprint_7.api_utils import generate_random_string

class TestLoginCourier:

    @allure.title("Успешная авторизация курьера (валидные данные)")
    @allure.description("Проверяет успешную авторизацию курьера с корректными логином и паролем и получение id.")
    def test_successful_login(self, courier):
        payload = {
            "login": courier["login"],
            "password": courier["password"]
        }
        response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', json=payload)
        assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
        assert "id" in response.json(), "В ответе нет id курьера"

    @allure.title("Авторизация с неверным логином")
    @allure.description("Проверяет, что система возвращает ошибку, если указан неверный логин.")
    def test_invalid_login_fails(self, courier):
        payload = {
            "login": generate_random_string(10),  # Случайный логин для теста
            "password": courier["password"]
        }
        response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', json=payload)
        assert response.status_code == 404, f"Ожидался код 404, получен {response.status_code}"
        assert response.json()["message"] == CourierMessages.ACCOUNT_NOT_FOUND, f"Ожидалось сообщение '{CourierMessages.ACCOUNT_NOT_FOUND}', получено {response.json().get('message')}"

    @allure.title("Авторизация с неверным паролем")
    @allure.description("Проверяет, что система возвращает ошибку, если указан неверный пароль.")
    def test_invalid_password_fails(self, courier):
        payload = {
            "login": courier["login"],
            "password": generate_random_string(10)  # Случайный пароль для теста
        }
        response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', json=payload)
        assert response.status_code == 404, f"Ожидался код 404, получен {response.status_code}"
        assert response.json()["message"] == CourierMessages.ACCOUNT_NOT_FOUND, f"Ожидалось сообщение '{CourierMessages.ACCOUNT_NOT_FOUND}', получено {response.json().get('message')}"

    @allure.title("Авторизация без логина")
    @allure.description("Проверяет, что система возвращает ошибку, если не указан логин.")
    def test_missing_login_fails(self, courier):
        payload = {
            "login": "",
            "password": courier["password"]
        }
        response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', json=payload)
        assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}"
        assert response.json()["message"] == CourierMessages.NOT_ENOUGH_DATA_FOR_LOGIN, f"Ожидалось сообщение '{CourierMessages.NOT_ENOUGH_DATA_FOR_LOGIN}', получено {response.json().get('message')}"

    @allure.title("Авторизация без пароля")
    @allure.description("Проверяет, что система возвращает ошибку, если не указан пароль.")
    def test_missing_password_fails(self, courier):
        payload = {
            "login": courier["login"],
            "password": ""
        }
        response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', json=payload)
        assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}"
        assert response.json()["message"] == CourierMessages.NOT_ENOUGH_DATA_FOR_LOGIN, f"Ожидалось сообщение '{CourierMessages.NOT_ENOUGH_DATA_FOR_LOGIN}', получено {response.json().get('message')}"