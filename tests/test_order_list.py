import allure
import requests
from data import Message, Url


class TestGetOrderList:
    @allure.title('проверка получения списка заказа')
    def test_get_order_list(self):
        response = requests.get(Url.ORDER_LIST)
        assert response.status_code == 200
        assert Message.LIST_ORDERS in response.text