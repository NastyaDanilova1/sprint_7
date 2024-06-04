import allure
import pytest
import requests
from data import *


class TestCreateOrder:
    @allure.title("создание заказа с разными цветами самоката")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["GREY", "BLACK"], []])
    def test_create_order_with_color(self,color):
        payload = UserData.user
        payload["color"] = color
        response = requests.post(Url.CREATE_ORDER, json=payload)

        assert response.status_code == 201
        assert response.status_code == 201 and Message.CREATE_ORDER in response.text
