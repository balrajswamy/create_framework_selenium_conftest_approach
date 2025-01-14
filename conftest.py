import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup_and_teardown(request):
    #global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    driver.quit()