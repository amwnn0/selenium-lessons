from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin

link = 'http://suninjuly.github.io/execute_script.html'


def calc(x):
    return log(abs(12 * sin(int(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    form = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", form)
    form.send_keys(str(calc(x)))
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    sleep(10)
    browser.quit()
