import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_hello(driver):
    text = driver.find_element(By.TAG_NAME, "h1").text
    assert text == "Hello from the Backend!"
    if text == "Hello from the Backend!":
        print("Integration between the frontend and backend services is Successful!")
    else:
        print("Integration between the frontend and backend services FAILED.")
