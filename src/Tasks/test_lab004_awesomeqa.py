import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("Testing the Radio buttons")
@allure.description("Verify all the buttons are clicked")
def test_Awesomeqa_Page():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Raagini")
    driver.find_element(By.XPATH,"//input[@id ='sex-1']").click()
    driver.find_element(By.XPATH,"//input[@id ='profession-1']").click()
    driver.find_element(By.XPATH,"//input[@id ='exp-2']").click()
    driver.find_element(By.XPATH,"//input[@id ='tool-2']").click()
    driver.find_element(By.XPATH,"//button[@class ='btn btn-info']").click()
    driver.close()
