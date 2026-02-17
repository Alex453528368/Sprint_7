import json
import allure
import pytest
import requests
from data_order import DataOrder
from endpoints import Endpoints
from urls import Urls


class TestOrderCreate:

    @allure.title('Проверка оформления заказа с разным набором цветов')
    @allure.description('Отправляем запрос на создание заказа с поочередным добавлением различных цветов и проверяем ответ')
    @pytest.mark.parametrize('color', [
        {"color": ["BLACK"]},
        {"color": ["GREY"]},
        {"color": ["BLACK", "GREY"]},
        {}
    ])
    def test_create_order_success(self, color):
        headers = {"Content-type": "application/json"}

        data = DataOrder.data.copy()
        data.update(color)

        response = requests.post(
            f'{Urls.QA_SCOOTER_URL}{Endpoints.create_order}',
            headers=headers,
            data=json.dumps(data)
        )

        assert response.status_code == 201
        assert "track" in response.text
