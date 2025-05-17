import pytest
from Sprint_7.api_utils import *

# Создаю фикстуру, чтобы создавать курьера перед тестом и удалять его после
@pytest.fixture(scope="function")
def courier():
    courier_data = generate_courier_data()
    response = register_new_courier_and_return_courier_data(courier_data['login'], courier_data['password'], courier_data['firstName'])
    assert response.get('ok') == True, f"Не удалось создать курьера: {response}"
    login_response = courier_login(courier_data['login'], courier_data['password'])
    assert login_response.status_code == 200, f"Не удалось авторизоваться, код ответа: {login_response.status_code}, текст: {login_response.text}"
    courier_id = login_response.json()['id']
    yield courier_data
    delete_courier(courier_id)