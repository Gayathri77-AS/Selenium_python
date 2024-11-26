from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

driver =  webdriver.Chrome()
driver.maximize_window()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.implicitly_wait(5)

try:
    uname_textbox = driver.find_element(By.ID,"username")
    uname_textbox.click()
    uname_textbox.send_keys("student")
    
    pswd_textbox =  driver.find_element(By.ID,"password")
    pswd_textbox.click()
    pswd_textbox.send_keys("Password123")
    
    submit_button = driver.find_element(By.XPATH,"//button[@id='submit']")
    submit_button.click()
    driver.implicitly_wait(5)

except Exception as e:
    print("Field not Found ",e)