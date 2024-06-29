import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function", autouse=True)
def login(driver):
    driver.get("http://192.168.39.133:32499/")
    