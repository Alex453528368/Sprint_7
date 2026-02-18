import pytest

from helps import Courier


# фикстура регистрации, авторизации и удаления курьера
import pytest
from helps import Courier


@pytest.fixture()
def courier():
    courier_api = Courier()

    courier_create = courier_api.courier_registration_in_the_system_and_get_courier_data()
    courier_login = courier_api.courier_login_in_the_system_and_get_id_courier(
        courier_create["data"]
    )
    yield {
        "id": courier_login["id"],
        "data": courier_create["data"]
    }
    courier_api.courier_subsequent_deletion(courier_login["id"])
