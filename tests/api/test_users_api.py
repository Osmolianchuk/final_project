"""
API Test Suite for User Management.

This module contains tests that verify the functionality of the user management
endpoints, including creation, retrieval, and updating of user data.
"""
import requests
class TestUsersAPI:
    """
    Test suite for validating the User API endpoints.
    This class contains methods to test the functionality of user-related API endpoints,
    including getting user details, creating a new user, and updating existing user data.
    Each test checks for correct API responses and successful data manipulation.

    Attributes:
    BASE_URL (str): URL of the base endpoint for user operations.
    """
    BASE_URL = 'https://api.example.com/users'    
    def test_get_user(self):
        """
        Test the GET user endpoint.
        Ensures that fetching a user by their ID returns a successful
        HTTP status and the correct user data.
        """
        response = requests.get(f"{self.BASE_URL}/123")
        assert response.status_code == 200
        assert response.json()['user']['id'] == 123

    def test_create_user(self):
        """
        Test the POST user endpoint.
        Verifies that creating a new user with valid data results in
        a successful HTTP status and the correct user instance creation.
        """
        user_data = {"name": "John Doe", "email": "john@example.com"}
        response = requests.post(self.BASE_URL, json=user_data)
        assert response.status_code == 201
        assert response.json()['user']['name'] == user_data['name']

    def test_update_user(self):
        """
        Test the PUT user endpoint.
        Confirms that updating existing user data results in the correct
        HTTP status and modified user instance.
        """
        updated_data = {"email": "newjohn@example.com"}
        response = requests.put(f"{self.BASE_URL}/123", json=updated_data)
        assert response.status_code == 200
        assert response.json()['user']['email'] == updated_data['email']
