from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

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

    driver.get("https://demo.automationtesting.in/Dynamic.html")
    src = driver.find_element(By.ID, "node")
    desti = driver.find_element(By.ID, "droparea")
    action_chains = ActionChains(driver)
    action_chains.drag_and_drop(src,desti).perform()
    driver.implicitly_wait(5)

except Exception as e:
    print("Field not Found ",e)