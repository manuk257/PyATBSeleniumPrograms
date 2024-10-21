import allure
import  time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
@allure.title("Verify the tittle of the Page Your Account Has Been Created!")
@allure.description("Verify the Continue button is clicked")
def test_loginPage_awesomwqa():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    firt_name = driver.find_element(By.XPATH,"//input[@id='input-firstname']")
    firt_name.send_keys("Manu")
    last_name = driver.find_element(By.XPATH,"//input[@id='input-lastname']")
    last_name.send_keys("Kumarr")
    email_cred = driver.find_element(By.XPATH,"//input[@id='input-email']")
    email_cred.send_keys("manu19773@gmail.com")
    telephone_num = driver.find_element(By.XPATH,"//input[@id='input-telephone']")
    telephone_num.send_keys("8753605125")
    Pass_textfeild = driver.find_element(By.XPATH,"//input[@id='input-password']")
    Pass_textfeild.send_keys("Hello@15432")
    password_confirm = driver.find_element(By.XPATH,"//input[@id='input-confirm']")
    password_confirm.send_keys("Hello@15432")
    Privacy_checkbox=driver.find_element(By.XPATH,"//input[@type='checkbox']")
    Privacy_checkbox.click()
    Login_button= driver.find_element(By.XPATH,"//input[@type='submit']")
    Login_button.click()
    page_title_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Your Account Has Been Created')]"))
    )
    actual_title = page_title_element.text
    expected_title = "Your Account Has Been Created!"
    assert actual_title == expected_title, f"Expected: {expected_title}, but got: {actual_title}"
    time.sleep(10)
    driver.back()
    driver.quit()




