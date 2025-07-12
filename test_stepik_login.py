from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = ""
password = ""


def test_stepik_login(browser):
    browser.implicitly_wait(2)
    browser.get('https://stepik.org/lesson/236895/step/1')
    # WebDriverWait
    browser.find_element(By.ID, 'ember479').click()
    # WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'id_login_email')))
    browser.find_element(By.ID, 'id_login_email').send_keys(email)
    browser.find_element(By.ID, 'id_login_password').send_keys(password)
    browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()
    # WebDriverWait(browser, 5).until(not EC.presence_of_element_located((By.ID, 'id_login_email')))
