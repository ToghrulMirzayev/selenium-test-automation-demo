from selenium.webdriver.common.by import By
from ui.elements.base_elements import InputElement, ActionElement

class LoginPage:
    """Page Object representing the login page"""

    username = InputElement((By.ID, "user-name"))
    password = InputElement((By.ID, "password"))
    login_button = ActionElement((By.ID, "login-button"))
    title_text = InputElement((By.CSS_SELECTOR, ".title"))
    error_text = InputElement((By.CSS_SELECTOR, ".error-message-container"))

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        """Logs in using the provided username and password"""
        self.username.clear()
        self.username.send_keys(username)
        self.password.clear()
        self.password.send_keys(password)
        self.login_button.click()

    def verify_main_title(self, expected):
        expected_result = expected
        actual_result = self.title_text.text
        assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"

    def verify_error_message(self, expected):
        expected_result = expected
        actual_result = self.error_text.text
        assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"

