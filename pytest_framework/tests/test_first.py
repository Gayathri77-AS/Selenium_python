import time
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from utils import config

def test_first(browser):
    browser.get(config.BASE_URL)
    login = LoginPage(browser)
    login.click_login_link()
    login.login(config.EMAIL, config.PASSWORD)
    time.sleep(2)
    
    home = HomePage(browser)
    home.click_search_link()
    home.search_product("shirt")
    time.sleep(2)
    
    product = ProductPage(browser)
    product.add_first_product_to_cart()
    time.sleep(2)
    product.view_cart()
    time.sleep(2)
    
    assert int(product.get_cart_count()) >= 1, "Cart should have atleast 1 item"