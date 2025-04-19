from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
    
    def add_first_product_to_cart(self):
        self.driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[1]").click()
    
    def view_cart(self):
        self.driver.find_element(By.XPATH, "//u[text() = 'View Cart']").click()
        
    def get_cart_count(self):
        return self.driver.find_element(By.CLASS_NAME, "cart_quantity").text
    