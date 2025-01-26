import requests
import pytest

class TestUsersAPI:
    BASE_URL = 'https://api.example.com/users'

    def test_get_user(self):
        response = requests.get(f"{self.BASE_URL}/123")
        assert response.status_code == 200
        assert response.json()['user']['id'] == 123

    def test_create_user(self):
        user_data = {"name": "John Doe", "email": "john@example.com"}
        response = requests.post(self.BASE_URL, json=user_data)
        assert response.status_code == 201
        assert response.json()['user']['name'] == user_data['name']

    def test_update_user(self):
        updated_data = {"email": "newjohn@example.com"}
        response = requests.put(f"{self.BASE_URL}/123", json=updated_data)
        assert response.status_code == 200
        assert response.json()['user']['email'] == updated_data['email']
