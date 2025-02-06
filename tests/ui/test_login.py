"""
Module for UI Testing with Selenium Integration.
"""
import logging
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class TestUsersUI(unittest.TestCase):
    """
    Test suite for validating the User interface on demoqa.com.
    This class contains methods to test user interaction through the UI,
    such as form submissions, button clicks, and text verifications.
    """

    def setUp(self):
        """ Setup before each test function execution. """
        # Assuming Chromedriver path is set in the PATH environment variable
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/")
        logging.info("Webdriver initialized and navigated to demoqa.com")

    def test_verify_user(self):
        """
        Verify user presence on UI.
        This test involves navigating to a specific part of the website,
        interacting with elements, and validating the output.
        """
        # Assuming there’s a link to 'Users' we need to click
        driver = self.driver
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Text Box"))
        ).click()

        # Assuming to find a specific username in an input field
        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "userName"))
        )
        username_input.send_keys("John Doe")
        username_input.send_keys(Keys.RETURN)  # Simulate hitting enter

        # Wait and verify some result on the page after input
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, "output"), "John Doe"  # Assuming 'output' is a result container ID
            )
        )

        logging.info('Username verified on UI.')
        self.assertIn("John Doe", driver.find_element(By.ID, "output").text)

    def tearDown(self):
        """ Clean up after each test function execution. """
        self.driver.quit()
        logging.info("Webdriver terminated.")

# Run the tests
if __name__ == "__main__":
    unittest.main()
