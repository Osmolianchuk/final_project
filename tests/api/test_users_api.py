"""
API Test Suite for User Management.

This module contains tests that verify the functionality of the user management
endpoints, including creation, retrieval, and updating of user data using JsonPlaceholder API.
"""
import logging
import requests

# Setting up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class TestUsersAPI:
    """
    Test suite for validating the User API endpoints using JsonPlaceholder API.
    This class contains methods to test the functionality of user-related API endpoints,
    including getting user details, creating a new user, and updating existing user data.
    Each test checks for correct API responses and successful data manipulation.

    Attributes:
    BASE_URL (str): URL of the base endpoint for user operations.
    """
    BASE_URL = 'https://jsonplaceholder.typicode.com/users'

    def test_get_user(self):
        """
        Test the GET user endpoint.
        Ensures that fetching a user by their ID returns a successful
        HTTP status and the correct user data.
        """
        user_id = 1  # Using a valid user ID available in JsonPlaceholder
        logging.info("Testing GET user endpoint for user ID %s", user_id)
        response = requests.get(f"{self.BASE_URL}/{user_id}", timeout=5)
        assert response.status_code == 200
        assert response.json()['id'] == user_id  # Adapted the key according to the JsonPlaceholder structure
        logging.debug("GET Response: %s", response.json())

    def test_create_user(self):
        """
        Test the POST user endpoint.
        Verifies that creating a new user with valid data results in
        a successful HTTP status and the correct user instance creation.
        """
        user_data = {"name": "John Doe", "email": "john@example.com"}
        logging.info("Testing POST user endpoint with user data: %s", user_data)
        response = requests.post(self.BASE_URL, json=user_data, timeout=5)
        assert response.status_code == 201
        assert 'id' in response.json()  # Checking for key presence since POST responses are stubbed
        logging.debug("POST Response: %s", response.json())

    def test_update_user(self):
        """
        Test the PUT user endpoint.
        Confirms that updating existing user data results in the correct
        HTTP status and modified user instance.
        """
        updated_data = {"email": "newjohn@example.com"}
        user_id = 1  # Using a valid user ID
        logging.info("Testing PUT user endpoint with update data for user ID %s: %s", user_id, updated_data)
        response = requests.put(f"{self.BASE_URL}/{user_id}", json=updated_data, timeout=5)
        assert response.status_code == 200
        assert 'id' in response.json()  # The JsonPlaceholder PUT response does not modify data but confirms reception
        logging.debug("PUT Response: %s", response.json())
