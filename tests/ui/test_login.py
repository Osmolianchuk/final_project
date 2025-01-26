from selenium import webdriver
import pytest

class TestLogin:
    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com/login")
        yield
        self.driver.quit()

    def test_valid_login(self, setup):
        self.driver.find_element_by_id("username").send_keys("user1")
        self.driver.find_element_by_id("password").send_keys("password")
        self.driver.find_element_by_id("submit").click()
        assert "Dashboard" in self.driver.title
