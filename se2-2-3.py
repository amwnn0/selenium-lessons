from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.select import Select

link = 'https://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    sleep(1)
    x1 = int(browser.find_element(By.ID, 'num1').text)
    x2 = int(browser.find_element(By.ID, 'num2').text)
    select = Select(browser.find_element(By.CLASS_NAME, 'custom-select'))
    select.select_by_visible_text(str(x1 + x2))
    browser.find_element(By.CLASS_NAME, 'btn').click()
finally:
    sleep(10)
    browser.quit()
