class UserData:

    user = {
        'firstname': 'Настя',
        'lastname': 'Данилова',
        'address': 'Санкт - Петербург',
        'metroStation': 3,
        'phone': '+79112498822',
        'rentTime': 2,
        'deliveryDate': '2024-08-11',
        'comment': '',
        'color': []

    }


class Url:
    MAIN_URL = 'http://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = f'{MAIN_URL}/api/v1/courier'
    CREATE_ORDER = f'{MAIN_URL}/api/v1/orders'
    ORDER_LIST = f'{MAIN_URL}/api/v1/orders'
    DELETE_COURIER = f'{MAIN_URL}/api/v1/courier/'
    GET_ORDER_TRACK = f'{MAIN_URL}/api/v1/orders/track'
    TAKE_ORDER = f'{MAIN_URL}/api/v1/orders/accept/'
    LOGIN_COURIER = f'{MAIN_URL}/api/v1/courier/login'


class Message:
    CREATE_COURIER = '{"ok":true}'
    CREATE_COURIER_TWICE = 'Этот логин уже используется'
    CREATE_COURIER_WITHOUT_LOGIN = 'Недостаточно данных для создания учетной записи'
    GET_ORDER = 'order'
    GET_ORDER_WITHOUT_TRACK = 'Недостаточно данных для поиска'
    GET_ORDER_FAKE_TRACK = 'Заказ не найден'
    DELETE_COURIER = '{"ok":true}'
    DELETE_COURIER_WITHOUT_ID = 'Not Found.'
    DELETE_COURIER_FAKE_ID = 'Курьера с таким id нет'
    LOGING_COURIER = 'id'
    LOGING_COURIER_WITHOUT_DATA = 'Недостаточно данных для входа'
    LOGING_COURIER_FAKE_DATA = 'Учетная запись не найдена'
    CREATE_ORDER = 'track'
    LIST_ORDERS = 'orders'
    TAKE_ORDER_FAKE_ID = 'Заказа с таким id не существует'
    TAKE_ORDER_FAKE_ID_COURIER = 'Курьера с таким id не существует'
    TAKE_ORDER_FAKE_TWICE = 'Этот заказ уже в работе'
    TAKE_ORDER_WITHOUT_ID_COURIER_ORDER = 'Недостаточно данных для поиска'
    TAKE_ORDER = '{"ok":true}'





