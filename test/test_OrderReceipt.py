import requests

class TestOrderReceipt:

    def test_successful_receipt_of_order(self, base_url, create_order):
        response = requests.get(base_url + f"orders/track?t={create_order}")
        assert response.status_code == 200, f"Status code 200 was expected and code {response.status_code} was returned."
        assert "order" in response.json(), f"order is missing from the server response."

    def test_without_an_order_number(self, base_url):
        response = requests.get(base_url + "orders/track")
        assert response.status_code == 400, f"Status code 400 was expected and code {response.status_code} was returned."
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для поиска'}, f"A {'code': 400, 'message': 'Недостаточно данных для поиска'} response was expected and a {response.json()} response was returned."

    def test_non_existent_order_number(self, base_url):
        response = requests.get(base_url + "orders/track?t=123456789")
        assert response.status_code == 404, f"Status code 404 was expected and code {response.status_code} was returned."
        assert response.json() == {'code': 404, 'message': 'Заказ не найден'}, f"A {'code': 404, 'message': 'Заказ не найден'} response was expected and a {response.json()} response was returned."

