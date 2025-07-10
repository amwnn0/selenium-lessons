from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    sleep(1)
    x = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CLASS_NAME, 'btn').click()
finally:
    sleep(10)
    browser.quit()
