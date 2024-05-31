
from data import Message
from for_help import *


class TestLoginCourier:
    @allure.title('проверка авторизации курьера')
    def test_login_courier(self):
        data = register_new_courier_and_return_login_password()
        response = requests.post(Url.LOGIN_COURIER, data={
            "login": data[0],
            "password": data[1],
        })
        assert response.status_code == 200
        assert Message.LOGING_COURIER in response.text
        delete_courier(data[0], data[1])


    @allure.title('проверка авторизации курьера без логина')
    def test_login_courier_without_login(self):
        response_create = register_new_courier_and_return_login_password()
        payload = {
            "login": "",
            "password":response_create,
        }
        response_post = requests.post(f'{Url.LOGIN_COURIER}', json=payload)
        assert response_post.status_code == 400
        assert Message.LOGING_COURIER_WITHOUT_DATA in response_post.text


    @allure.title('проверка авторизации курьера без пароля')
    def test_login_courier_without_password(self):
        data = register_new_courier_and_return_login_password()
        response = requests.post(Url.LOGIN_COURIER, data={
            "login": '',
            "password": data[1],
        })
        assert response.status_code == 400
        assert Message.LOGING_COURIER_WITHOUT_DATA in response.text


    @allure.title('проверка авторизации курьера без логина и пароля')
    def test_login_courier_without_password_and_login(self):
        response = requests.post(Url.LOGIN_COURIER, data={
            "login": '',
            "password": '',
        })
        assert response.status_code == 400
        assert Message.LOGING_COURIER_WITHOUT_DATA in response.text


    @allure.title('проверка авторизации с несуществующими данными')
    def test_login_courier_with_fake_data(self):
        response = requests.post(Url.LOGIN_COURIER, data={
            "login": 'nastya',
            "password": 'newcourier',
        })
        assert response.status_code == 404
        assert Message.LOGING_COURIER_FAKE_DATA in response.text