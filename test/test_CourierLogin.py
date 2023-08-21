import requests
from log import logger_setup
import os


log_file_path = os.path.join('C://Users//1//Desktop//INTEXSOFT//api_test//log', 'courier_login_log.log')
logger = logger_setup.setup_logger("DeleteLogger", log_file_path)


class TestLoginСapability:

 def test_the_courier_can_log_in(self, login_courier, base_url):
    json_data = {
    "login": "Vasiliy",
    "password": "1234"
    }
    response = requests.post(base_url + "courier/login", data=json_data)
    assert response.status_code == 200, f"Status code 200 was expected and code {response.status_code} was returned."
    assert response.json() == {'id': login_courier}, f"A {'id': login_courier} response was expected and a {response.json()} response was returned."

class TestWithoutData:

 def test_login_without_login(self, base_url):
    json_data = {
    "password": "1234"
    }
    response = requests.post(base_url + "courier/login", data=json_data)
    assert response.status_code == 400, f"Status code 400 was expected and code {response.status_code} was returned."
    assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}, f"A {'code': 400, 'message': 'Недостаточно данных для входа'} response was expected and a {response.json()} response was returned."

 def test_login_without_password(self, base_url):
    logger.info("Testing order acceptance without order ID")
    json_data = {
    "login": "Vasiliy"
    }
    response = requests.post(base_url + "courier/login", data=json_data)
    logger.debug(f"Status code {response.status_code} was returned and message{response.json()}")
    assert response.status_code == 400, f"Status code 400 was expected and code {response.status_code} was returned."
    assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}, f"A {'code': 400, 'message': 'Недостаточно данных для входа'} response was expected and a {response.json()} response was returned."


class TestEnteringNonExistentData:

 def test_invalid_logs(self, base_url):
    json_data = {
    "login": "Inanko",
    "password": "1234"
    }
    response = requests.post(base_url + "courier/login", data=json_data)
    assert response.status_code == 404, f"Status code 404 was expected and code {response.status_code} was returned."
    assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}, f"A {'code': 404, 'message': 'Учетная запись не найдена'} response was expected and a {response.json()} response was returned."

 def test_invalid_password(self, base_url):
    json_data = {
    "login": "Vasiliy",
    "password": "123456788"
    }
    response = requests.post(base_url + "courier/login", data=json_data)
    assert response.status_code == 404, f"Status code 404 was expected and code {response.status_code} was returned."
    assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}, f"A {'code': 404, 'message': 'Учетная запись не найдена'} response was expected and a {response.json()} response was returned."





