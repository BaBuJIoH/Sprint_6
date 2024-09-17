import pytest
from selenium import webdriver
from links import Links

@pytest.fixture(scope="function")
def driver():
    # Инициализация Firefox WebDriver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Links.BASE_URL)
    yield driver
    driver.quit()
