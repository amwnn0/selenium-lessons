import math
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = ""
password = ""
links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1',
         ]


def func():
    return math.log(int(time.time()))


@pytest.mark.parametrize('link', links)
def test_stepik_login(browser, link):
    browser.implicitly_wait(10)
    browser.get(link)
    browser.find_element(By.ID, 'ember479').click()
    browser.find_element(By.ID, 'id_login_email').send_keys(email)
    browser.find_element(By.ID, 'id_login_password').send_keys(password)
    browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()
    WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.ID, 'id_login_email')))
    browser.find_element(By.CLASS_NAME, 'textarea').send_keys(func())
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))
    assert browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text == "Correct!"
