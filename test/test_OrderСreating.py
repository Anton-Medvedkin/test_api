import requests
import pytest

class TestCreatingOrder:

 @pytest.mark.parametrize("color", [None, "BLACK", "GRAY", "BLACK_GRAY"])
 def test_with_color(self, color, base_url):
    json_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }

    if color == "BLACK_GRAY":
        json_data["color"] = ["BLACK", "GRAY"]
    elif color is not None:
        json_data["color"] = [color]

    response = requests.post(base_url + "orders", json=json_data)
    assert response.status_code == 201, f"Status code 201 was expected and code {response.status_code} was returned."
    response_data = response.json()
    assert "track" in response_data, f"track is missing from the server response."
    assert isinstance(response_data["track"], int), f"track is not an integer."