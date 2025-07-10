from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import sin, log


def calc(x):
    return log(abs(12 * sin(int(x))))


link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button').click()
    sleep(1)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(str(calc(x)))
    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click()

finally:
    sleep(10)
    browser.quit()
