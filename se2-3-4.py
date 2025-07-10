from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin

link = "https://suninjuly.github.io/alert_accept.html"


def calc(x):
    return log(abs(12 * sin(int(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CLASS_NAME, 'btn').click()
    browser.switch_to.alert.accept()
    sleep(1)
    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(str(calc(x)))
    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    sleep(10)
    browser.quit()
