import requests

class TestListOrders:

 def test_list_order(self, base_url):
    response = requests.get(base_url + "orders")
    order_data = response.json()

    assert response.status_code == 200, f"Status code 200 was expected and code {response.status_code} was returned."
    assert "orders" in order_data, f"orders is missing from the server response."
    assert isinstance(order_data["orders"], list), f"orders is not an list."