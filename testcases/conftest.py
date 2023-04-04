from selenium import webdriver
import pytest
@pytest.fixture()
def setup():
    yield
    driver.close()
