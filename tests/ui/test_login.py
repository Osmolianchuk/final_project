import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui.WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO, filename='test_log.log', filemode='w', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def wait_for_ready_state_full(driver, timeout=30):
    """
    Waits until the web page's document ready state is 'complete'.
    
    This function polls the document.readyState until it equals 'complete',
    indicating that the page has fully loaded including stylesheets, images, and subframes.
    
    Parameters:
    - driver: The WebDriver object currently controlling the browser.
    - timeout: Maximum time in seconds to wait for the page to load, defaults to 30 seconds.
    
    Returns:
    None
    """
    WebDriverWait(driver, timeout).until(
        lambda x: driver.execute_script("return document.readyState === 'complete'")
    )
    logging.info("Page fully loaded.")

def test_submit_text_form():
    """
    Performs a test to interact with a web form, fill, and submit it.
    
    This test automates the process of opening a web form, filling the fields with predetermine data,
    submitting the form, and finally, closing the browser. Logging is used to record the steps and results.
    
    Uses global configurations for the WebDriver and assumes specific IDs for elements.
    
    Returns:
    None
    """
    logging.info("Starting the test.")
    
    # Initialize the WebDriver for Chrome
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    
    logging.info("Opened webpage: https://demoqa.com/text-box")
    
    # Wait for the full initial loading of the page
    wait_for_ready_state_full(driver)

    # Refresh the page after the initial load
    driver.refresh()
    logging.info("Page refreshed.")

    # Wait again for the page to be fully loaded after the refresh
    wait_for_ready_state_full(driver)
    
    try:
        # Wait until the first input field (userName) is visible on the page
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "userName"))
        )
        logging.info("Input field for userName is visible.")

        # Send input to the text box fields
        driver.find_element(By.ID, "userName").send_keys("John Doe")
        driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("1234 Street City")
        driver.find_element(By.ID, "permanentAddress").send_keys("5678 Avenue City")
        logging.info("Form fields filled with data.")

        # Submit the form
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        logging.info("Form submitted.")

    finally:
        # Close the browser to free up resources
        driver.quit()
        logging.info("Web browser closed.")

if __name__ == "__main__":
    pytest.main()
