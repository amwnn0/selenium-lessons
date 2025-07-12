from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


# pytest -v --tb=line --reruns 1 --browser_name=chrome --language=es test_items.py
def test_button_addtobasket_exists(browser):
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
