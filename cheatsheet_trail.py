from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

chrome_driver_path = "D:\\webdrivers\\chromedriver-win64\\chromedriver.exe"
chrome_service = ChromeService(chrome_driver_path)
chrome_driver = webdriver.Chrome(service=chrome_service)
chrome_driver.get("https://www.google.com")
print("Chrome Page title is:", chrome_driver.title)
chrome_driver.quit()

firefox_driver_path = "D:\\webdrivers\\geckodriver-win64\\geckodriver.exe"
firefox_service = FirefoxService(firefox_driver_path)
firefox_driver =  webdriver.Firefox(service=firefox_service)
firefox_driver.get("https://www.google.com")
print("Firefox Page title is:", firefox_driver.title)
firefox_driver.quit()

edge_driver_path = "D:\\webdrivers\\edgedriver-win64\\msedgedriver.exe"
edge_service = EdgeService(edge_driver_path)
edge_driver =  webdriver.Edge(service=edge_service)
edge_driver.get("https://www.google.com")
print("Edge Page title is:", edge_driver.title)
edge_driver.quit()
