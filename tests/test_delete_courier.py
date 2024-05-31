import random
import allure
import requests
from const import Const, MessageText
from conftest import create_courier


class TestDeleteCourier:
    @allure.title('проверка удаления курьера со всеми обязательными полями')
    def test_delete_courier(self, create_courier):
        response_delete = requests.delete(f'{Const.DELETE_COURIER}{create_courier}')
        assert response_delete.status_code == 200
        assert MessageText.DELETE_COURIER in response_delete.text

    @allure.title('проверка удаления курьера с несуществующим id курьера')
    def test_delete_courier_with_fake_id(self):
        random_id = random.randint(12, 1231232)
        response_delete = requests.delete(f'{Const.DELETE_COURIER}{random_id}')
        assert response_delete.status_code == 404
        assert MessageText.DELETE_COURIER_FAKE_ID in response_delete.text


    @allure.title('проверка удаления курьера без указания id курьера')
    def test_delete_courier_without_id(self):
        response_delete = requests.delete(Const.DELETE_COURIER)
        assert response_delete.status_code == 404
        assert MessageText.DELETE_COURIER_WITHOUT_ID in response_delete.text
        # здесь баг, ответ не совпадает со свагером


