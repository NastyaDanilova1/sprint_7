import allure
import requests
import random
import string
from data import Url



# метод генерации строки из букв нижнего регистра
def random_string(length):
    return (f"{''.join(random.choice(string.ascii_lowercase) for i in range(length))}")

    # метод генерации логина, пароля и имени
def generate_data():
    login = random_string(10)
    first_name = random_string(10)
    password = random_string(10)

    return first_name, login, password


@allure.step('создаем курьера и получаем имя, пароль и логин')
def register_new_courier_and_return_login_password():
    login_pass = []

    login = random_string(10)
    first_name = random_string(10)
    password = random_string(10)


    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(Url.CREATE_COURIER, data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass

@allure.step('удаление курьера')
def delete_courier(login, password):
    response_post = requests.post(Url.LOGIN_COURIER, data={
        "login": login,
        "password": password,
    })
    courier_id = response_post.json()['id']
    requests.delete(f'{Url.DELETE_COURIER}/{courier_id}')



