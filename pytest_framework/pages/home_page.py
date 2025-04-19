from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        
    def click_search_link(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Products')]").click()
    
    def search_product(self, product_name):
        self.driver.find_element(By.ID, "search_product").send_keys(product_name)
        self.driver.find_element(By.ID, "submit_search").click()