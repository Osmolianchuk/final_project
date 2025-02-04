import logging
import requests

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
        logging.info("Testing GET user endpoint for user ID 123")
        response = requests.get(f"{self.BASE_URL}/123", timeout=5)
        
        try:
            response.raise_for_status()
            logging.debug("Received response: %s", response.json())
        except requests.exceptions.HTTPError as err:
            logging.error("HTTP error occurred: %s - Status code: %s", err, response.status_code)
            raise
        except requests.exceptions.RequestException as err:
            logging.error("Error occurred: %s", err)
            raise
        
        assert response.status_code == 200
        assert response.json()['user']['id'] == 123
        logging.info("GET user endpoint test passed.")

    def test_create_user(self):
        """
        Test the POST user endpoint.
        Verifies that creating a new user with valid data results in
        a successful HTTP status and the correct user instance creation.
        """
        user_data = {"name": "John Doe", "email": "john@example.com"}
        logging.info("Testing POST user endpoint with data: %s", user_data)
        response = requests.post(self.BASE_URL, json=user_data, timeout=5)

        try:
            response.raise_for_status()
            logging.debug("Received response: %s", response.json())
        except requests.exceptions.HTTPError as err:
            logging.error("HTTP error occurred: %s - Status code: %s", err, response.status_code)
            raise
        except requests.exceptions.RequestException as err:
            logging.error("Error occurred: %s", err)
            raise

        assert response.status_code == 201
        assert response.json()['user']['name'] == user_data['name']
        logging.info("POST user endpoint test passed.")

    def test_update_user(self):
        """
        Test the PUT user endpoint.
        Confirms that updating existing user data results in the correct
        HTTP status and modified user instance.
        """
        updated_data = {"email": "newjohn@example.com"}
        logging.info("Testing PUT user endpoint with data: %s", updated_data)
        response = requests.put(f"{self.BASE_URL}/123", json=updated_data, timeout=5)

        try:
            response.raise_for_status()
            logging.debug("Received response: %s", response.json())
        except requests.exceptions.HTTPError as err:
            logging.error("HTTP error occurred: %s - Status code: %s", err, response.status_code)
            raise
        except requests.exceptions.RequestException as err:
            logging.error("Error occurred: %s", err)
