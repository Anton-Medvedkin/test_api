import requests
from log import logger_setup
import os


log_file_path = os.path.join('C://Users//1//Desktop//INTEXSOFT//api_test//log', 'order_acceptance_log.log')
logger = logger_setup.setup_logger("DeleteLogger", log_file_path)


class TestOrderAcceptance:

    def test_successful_order_acceptance(self, login_courier, base_url, create_order_id):
        response = requests.put(base_url + f"orders/accept/{create_order_id}?courierId={login_courier}")
        assert response.status_code == 200, f"Status code 200 was expected and code {response.status_code} was returned."
        assert response.json() == {'ok': True}, f"A {'ok': True} response was expected and a {response.json()} response was returned."

class TestWithNonExistentParameters:

    def test_accepting_an_order_with_non_existent_courier_id(self, base_url, create_order_id):
        response = requests.put(base_url + f"orders/accept/{create_order_id}?courierId=2000200200")
        assert response.status_code == 404, f"Status code 404 was expected and code {response.status_code} was returned."
        assert response.json() == {'code': 404, 'message': 'Курьера с таким id не существует'}, f"A {'code': 404, 'message': 'Курьера с таким id не существует'} response was expected and a {response.json()} response was returned."

    def test_accepting_an_order_with_non_existent_order_id(self, login_courier, base_url):
        response = requests.put(base_url + f"orders/accept/454684?courierId={login_courier}")
        assert response.status_code == 404, f"Status code 404 was expected and code {response.status_code} was returned."
        assert response.json() == {'code': 404, 'message': 'Заказа с таким id не существует'}, f"A {'code': 404, 'message': 'Заказа с таким id не существует'} response was expected and a {response.json()} response was returned."

class TestWithoutParameters:

    def test_order_acceptance_without_courier_id(self, base_url, create_order_id):
        response = requests.put(base_url + f"orders/accept/{create_order_id}")
        assert response.status_code == 400, f"Status code 400 was expected and code {response.status_code} was returned."
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для поиска'}, f"A {'code': 400, 'message': 'Недостаточно данных для поиска'} response was expected and a {response.json()} response was returned."

    def test_order_acceptance_without_order_id(self, login_courier, base_url):
        logger.info("Testing order acceptance without order ID")
        response = requests.put(base_url + f"orders/accept/?courierId={login_courier}")
        logger.debug(f"Status code {response.status_code} was returned and message{response.json()}")
        assert response.status_code == 400, f"Status code 400 was expected and code {response.status_code} was returned."
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для поиска'}, f"A {'code': 400, 'message': 'Недостаточно данных для поиска'} response was expected and a {response.json()} response was returned."

