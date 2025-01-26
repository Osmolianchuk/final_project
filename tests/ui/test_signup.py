from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("driver_init")
class TestSignup:
    URL = "https://example.com/signup"

    def go_to_signup_page(self):
        self.driver.get(self.URL)

    def test_valid_signup(self):
        self.go_to_signup_page()
        self.driver.find_element_by_id("username").send_keys("newuser")
        self.driver.find_element_by_id("email").send_keys("newuser@example.com")
        self.driver.find_element_by_id("password").send_keys("securepassword123")
        self.driver.find_element_by_id("submit").click()
        success_message = self.driver.find_element_by_id("success").text
        assert "Welcome" in success_message

    def test_signup_existing_user(self):
        self.go_to_signup_page()
        self.driver.find_element_by_id("username").send_keys("existinguser")
        self.driver.find_element_by_id("email").send_keys("existinguser@example.com")
        self.driver.find_element_by_id("password").send_keys("password")
        self.driver.find_element_by_id("submit").click()
        error_message = self.driver.find_element_by_id("error").text
        assert "User already exists" in error_message

    def test_signup_with_invalid_email(self):
        self.go_to_signup_page()
        self.driver.find_element_by_id("username").send_keys("testuser")
        self.driver.find_element_by_id("email").send_keys("notanemail")
        self.driver.find_element_by_id("password").send_keys("password123")
        self.driver.find_element_by_id("submit").click()
        validation_message = self.driver.find_element_by_id("email_error").text
        assert "Invalid email" in validation_message
