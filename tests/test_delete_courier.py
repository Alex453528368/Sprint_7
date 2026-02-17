import allure
from helps import Courier


class TestDeleteCourier:

    @allure.title('Проверка удаления курьера') 
    @allure.description('Отправляем запрос на удаление курьера и проверяем ответ')
    def test_delete_courier_success(self):
        courier_api = Courier()
        courier_data = courier_api.courier_registration_in_the_system_and_get_courier_data()["data"]
        courier_id = courier_api.courier_login_in_the_system_and_get_id_courier(courier_data)["id"]
        response = courier_api.courier_subsequent_deletion(courier_id)
        assert response["status_code"] == 200
        assert response["response_text"] == '{"ok":true}'


    @allure.title('Проверка удаления курьера с')
    @allure.description('Отправляем запрос на удаление курьера с несущ.ID и проверяем ответ')
    def test_delete_courier_invalid_id_failed(self):
        courier_id = '123456'
        response = Courier().courier_subsequent_deletion(courier_id)
        assert response["status_code"] == 404
        assert "Курьера с таким id нет" in response["response_text"] 

    @allure.title('Проверка создания нового курьера')
    @allure.description('Отправляем запрос на удаление курьера без ID и проверяем ответ')
    def test_delete_courier_none_id_failed(self):
        courier_id = None
        response = Courier().courier_subsequent_deletion(courier_id)
        assert response["status_code"] == 500
        assert "invalid input syntax" in response["response_text"] 
