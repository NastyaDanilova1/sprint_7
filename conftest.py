import pytest
from data import UserData
from for_help import *


@pytest.fixture(scope='function')
def create_courier():
    data = register_new_courier_and_return_login_password()

    response_post = requests.post(Url.LOGIN_COURIER, data={
        "login": data[0],
        "password": data[1],
    })
    courier_id = response_post.json()['id']
    yield courier_id
    requests.delete(f'{Url.DELETE_COURIER}/{courier_id}')


