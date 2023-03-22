import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from ui.pages.login_page import LoginPage



@pytest.fixture
def get_chrome_options():
    options = ChromeOptions()
    options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    options.add_argument('chrome')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome(options=get_chrome_options, service=Service(ChromeDriverManager().install()))
    return driver


@pytest.fixture
def setup(get_webdriver):
    url = 'https://www.saucedemo.com/'
    get_webdriver.get(url)
    yield get_webdriver
    get_webdriver.quit()

@pytest.fixture
def login_page(setup):
    yield LoginPage(setup)
