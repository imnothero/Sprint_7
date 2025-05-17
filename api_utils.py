# Файл с утилитами для работы с API Яндекс Самоката
import requests
import string
import random
import allure
from api_urls import MAIN_URL, CREATE_COURIER_URL, LOGIN_COURIER_URL, DELETE_COURIER_URL

@allure.step("Регистрация нового курьера")
def register_new_courier_and_return_courier_data(login, password, first_name):
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)
    return response.json() if response.status_code == 201 else {}

def generate_random_string(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))

def generate_courier_data():
    courier_data = {}
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    courier_data["login"] = login
    courier_data["password"] = password
    courier_data["firstName"] = first_name
    return courier_data

@allure.step("Авторизация курьера")
def courier_login(login, password):
    payload = {"login": login, "password": password}
    response = requests.post(f"{MAIN_URL}{LOGIN_COURIER_URL}", json=payload)
    if response.status_code == 200:
        return response
    return None

@allure.step("Удаление курьера")
def delete_courier(id):
    requests.delete(f"{MAIN_URL}{DELETE_COURIER_URL}{id}")