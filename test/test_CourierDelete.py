import requests
#from log import logger_setup
# import os
#
#
# log_file_path = os.path.join('C://Users//1//Desktop//INTEXSOFT//api_test//log', 'delete_log.log')
# logger = logger_setup.setup_logger("DeleteLogger", log_file_path)


class TestDeleteCourier:

    def test_successful_deletion(self, delete_courier):
        assert delete_courier.status_code == 200, f"Status code 200 was expected and code {delete_courier.status_code} was returned."
        assert delete_courier.json() == {'ok': True}, f"A {'ok': True} response was expected and a {delete_courier.json()} response was returned."

    def test_deletion_with_invalid_id(self, base_url):
        id = 12345678
        response = requests.delete(base_url + f"courier/{id}")
        assert response.status_code == 404, f"Status code 404 was expected and code {response.status_code} was returned."
        assert response.json() == {'code': 404, 'message': 'Курьера с таким id нет.'}, f"A {'code': 404, 'message': 'Курьера с таким id нет.'} response was expected and a {response.json()} response was returned."

    def test_deletion_without_id(self, base_url):
       # logger.info("Testing courier deletion without ID")
        response = requests.delete(base_url + f"courier/")
       # logger.debug(f"Status code {response.status_code} was returned and message{response.json()}")
        assert response.status_code == 400, f"Status code 400 was expected and code {response.status_code} was returned."
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для удаления курьера'}, f"A {'code': 400, 'message': 'Недостаточно данных для удаления курьера'} response was expected and a {response.json()} response was returned."
