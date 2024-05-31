import allure
import requests
from const import MessageText, Const
from for_help import *




class TestCreateCourier:
    @allure.title('курьера можно создать со всеми обязательными полями')
    def test_create_courier(self):
        login, password, first_name = generate_data()
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(Const.CREATE_COURIER, data=payload)
        assert response.status_code == 201
        assert MessageText.CREATE_COURIER in response.text
        delete_courier(login, password)


    @allure.title('невозможно создать двух одинаковых курьеров')
    def test_create_courier_twice(self):
        data = register_new_courier_and_return_login_password()
        response = requests.post(Const.CREATE_COURIER, data={
            "login": data[0],
            "password": data[1],
            "firstName": data[2]
        })
        assert response.status_code == 409
        assert MessageText.CREATE_COURIER_TWICE in response.text

    @allure.title('создание курьера без имени')
    def test_create_courier_without_first_name(self):
        login, password, first_name = generate_data()
        payload = {
            "login": login,
            "password": password,
        }
        response = requests.post(Const.CREATE_COURIER, data=payload)
        assert response.status_code == 201
        assert MessageText.CREATE_COURIER in response.text
        delete_courier(login, password)


    @allure.title('создание курьера без логина')
    def test_create_courier_without_login(self):
        login, password, first_name = generate_data()
        payload = {
            "password": password,
            "firstName": first_name
        }

        response = requests.post(Const.CREATE_COURIER, data=payload)
        assert response.status_code == 400
        assert MessageText.CREATE_COURIER_WITHOUT_LOGIN in response.text


    @allure.title('создание курьера без пароля')
    def test_create_courier_without_password(self):
        login, password, first_name = generate_data()
        payload = {
            "login": login,
            "firstName": first_name
        }
        response = requests.post(Const.CREATE_COURIER, data=payload)
        assert response.status_code == 400
        assert MessageText.CREATE_COURIER_WITHOUT_LOGIN in response.text


