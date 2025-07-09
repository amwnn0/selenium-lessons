from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = 'http://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    for element in elements:
        element.send_keys("Мой ответ")
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    sleep(10)
    browser.quit()