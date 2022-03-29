from selenium.webdriver.common.by import By
import time


def test_add_to_basket_btn_is_present(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(add_to_basket_button) is not None, "Add to basket button is not displayed"
