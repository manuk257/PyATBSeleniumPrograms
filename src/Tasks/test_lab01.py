import allure
from selenium import webdriver
import pytest

@allure.title("Verify the tittle of the webpage app.VWO.com")
def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    driver.title
    assert driver.current_url== "https://www.flipkart.com/"