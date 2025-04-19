from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

#service = Service("C:/Users/user/Downloads/geckodriver-v0.35.0-win-aarch64")

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Firefox(options=options)

driver.get("https://www.google.com")

driver.quit()