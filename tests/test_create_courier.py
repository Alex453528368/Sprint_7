import allure
import pytest
import requests
from helps import DataCourier, DataCreateCourier, Courier
from endpoints import Endpoints
from urls import Urls
from helps import DataCreateCourier


class TestCreateCourier:

    @allure.title('Проверка создания нового курьера') 
    @allure.description('Отправляем запрос на создание курьера, проверяем ответ и удаляем созданного курьера')
    def test_registration_courier_success(self):
        data = DataCreateCourier.generating_fake_valid_data_to_create_courier()
        response_body = '{"ok":true}'
        response = requests.post(
        f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}',data=data)
        assert response.status_code == 201
        assert response.text == response_body
        # очистка БД
        courier_id = Courier().courier_login_in_the_system_and_get_id_courier(data)["id"]
        Courier().courier_subsequent_deletion(courier_id)

    @allure.title('Проверка ошибки при создании двух одинаковых курьеров')
    @allure.description('Отправляем повторный запрос на создание курьера, проверяем ответ и удаляем курьера')
    def test_registration_double_courier_failed(self, courier):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}', data=courier["data"])
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.text

    @allure.title('Проверка ошибки при создании курьера без заполнения обязательных полей Login/Password')
    @allure.description('Отправляем запрос на создание курьера без заполнения обязательных полей Login/Password и проверяем ответ')
    @pytest.mark.parametrize('courier_data', [DataCourier.invalid_data_login_without_login,
                                           DataCourier.invalid_data_login_without_password])
    def test_courier_registration_without_parameters_failed(self, courier_data):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}', data=courier_data)
        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.text
