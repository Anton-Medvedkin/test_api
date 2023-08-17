import pytest
import requests


@pytest.fixture()
def create_courier():
    json_data = {
        "login": "Vasiliy",
        "password": "1234",
        "firstName": "vasia"
    }
    response = requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier", data=json_data)
    yield response
    json_data = {
        "login": "Vasiliy",
        "password": "1234"
    }
    response = requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=json_data)
    data = response.json()
    id = data['id']
    requests.delete(f"http://qa-scooter.praktikum-services.ru/api/v1/courier/{id}")

@pytest.fixture()
def login_courier():
    json_data = {
        "login": "Vasiliy",
        "password": "1234",
        "firstName": "vasia"
    }
    requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier", data=json_data)
    json_data = {
        "login": "Vasiliy",
        "password": "1234"
    }
    response = requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=json_data)
    data = response.json()
    id = data['id']
    yield id
    requests.delete(f"http://qa-scooter.praktikum-services.ru/api/v1/courier/{id}")

@pytest.fixture()
def delete_courier():
    json_data = {
        "login": "Vasiliy",
        "password": "1234",
        "firstName": "vasia"
    }
    requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier", data=json_data)
    json_data = {
        "login": "Vasiliy",
        "password": "1234"
    }
    response = requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=json_data)
    data = response.json()
    id = data['id']
    response = requests.delete(f"http://qa-scooter.praktikum-services.ru/api/v1/courier/{id}")
    yield response

@pytest.fixture()
def create_order(base_url):
    json_data = {
    "firstName": "Anton",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
    }
    response = requests.post(base_url + "orders", json=json_data)
    return response.json()['track']

@pytest.fixture()
def create_order_id(base_url):
    json_data = {
        "firstName": "Antonio",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }
    response = requests.post(base_url + "orders", json=json_data)
    track = response.json()['track']
    response = requests.get(base_url + f"orders/track?t={track}")
    return response.json()['order']['id']

@pytest.fixture()
def base_url():
    return "http://qa-scooter.praktikum-services.ru/api/v1/"





