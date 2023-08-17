import requests

class TestCreateСapability:

 def test_can_create_a_courier(self, create_courier):
       assert create_courier.status_code == 201, f"Status code 201 was expected and code {create_courier.status_code} was returned."
       assert create_courier.json() == {'ok': True}, f"A {'ok': True} response was expected and a {create_courier.json()} response was returned."

class TestInabilityToCreate:

 def test_two_identical_couriers(self, create_courier, base_url):
    json_data = {
        "login": "Vasiliy",
        "password": "1234",
        "firstName": "vasia"
    }
    response = requests.post(base_url + "courier", data=json_data)
    assert response.status_code == 409, f"Status code 409 was expected and code {response.status_code} was returned."
    assert response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}, f"A {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'} response was expected and a {response.json()} response was returned."

class TestWithoutDate:

 def test_create_without_login(self, base_url):
    json_data = {
        "password": "1234",
        "firstName": "saske"
    }
    response = requests.post(base_url + "courier", data=json_data)
    assert response.status_code == 400, f"Status code 400 was expected and code {response.status_code} was returned."
    assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}, f"A {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'} response was expected and a {response.json()} response was returned."

 def test_create_without_password(self, base_url):
    json_data = {
        "login": "yura",
        "firstName": "saske"
    }
    response = requests.post(base_url + "courier", data=json_data)
    assert response.status_code == 400, f"Status code 400 was expected and code {response.status_code} was returned."
    assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}, f"A {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'} response was expected and a {response.json()} response was returned."
















 #def test_create_without_firstName(self, base_url):
 #   json_data = {
 #       "login": "yura",
 #       "password": "1234"
 #   }
 #   response = requests.post(base_url + "courier", data=json_data)
 #   assert response.status_code == 400, f"Status code 400 was expected and code {response.status_code} was returned."
 #   assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}, f"A {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'} response was expected and a {response.json()} response was returned."

