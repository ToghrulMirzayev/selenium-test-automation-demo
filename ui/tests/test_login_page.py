import pytest
from config import LoginScenarios, data


def test_successful_login(login_page):
    login_page.login(data.CORRECT_USERNAME, data.CORRECT_PASSWORD)
    login_page.verify_main_title(data.MAIN_TITLE)


@pytest.mark.parametrize("username, password, expected_text",
                         (LoginScenarios.login_incorrect_password, LoginScenarios.login_empty_username,
                          LoginScenarios.login_locked_username))
def test_login(login_page, username, password, expected_text):
    login_page.login(username=username, password=password)
    login_page.verify_error_message(expected_text)
