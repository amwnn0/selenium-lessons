from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "text.txt")
link = 'https://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.NAME, 'firstname').send_keys('John')
    browser.find_element(By.NAME, 'lastname').send_keys('Smith')
    browser.find_element(By.NAME, 'email').send_keys('<EMAIL>')
    browser.find_element(By.ID, 'file').send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, 'button').click()

finally:
    sleep(10)
    browser.quit()
