import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service
from ui.pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store")


@pytest.fixture
def get_browser(request):
    browser = request.config.getoption("--browser")
    return browser


@pytest.fixture
def select_browser(get_browser):
    if get_browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    else:
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    return driver


@pytest.fixture
def setup(select_browser):
    url = "https://www.saucedemo.com/"
    select_browser.get(url)
    yield select_browser
    select_browser.quit()


@pytest.fixture
def login_page(setup):
    yield LoginPage(setup)
