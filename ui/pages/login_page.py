from selenium.webdriver.common.by import By
from ui.elements.base_elements import InputElement, ActionElement


class LoginPage:
    """Page Object representing the login page"""

    USERNAME = InputElement((By.ID, "user-name"))
    PASSWORD = InputElement((By.ID, "password"))
    LOGIN_BTN = ActionElement((By.ID, "login-button"))
    TITLE_TEXT = InputElement((By.CSS_SELECTOR, ".title"))
    ERROR_TEXT = InputElement((By.CSS_SELECTOR, ".error-message-container"))

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        """Logs in using the provided username and password"""
        self.USERNAME.clear()
        self.USERNAME.send_keys(username)
        self.PASSWORD.clear()
        self.PASSWORD.send_keys(password)
        self.LOGIN_BTN.click()

    def verify_main_title(self, expected):
        expected_result = expected
        actual_result = self.TITLE_TEXT.text
        assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"

    def verify_error_message(self, expected):
        expected_result = expected
        actual_result = self.ERROR_TEXT.text
        assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"
