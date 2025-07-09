from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = "https://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    sleep(1)

    field1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    field1.send_keys("John")
    field2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    field2.send_keys("John")
    field3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
    field3.send_keys("John")

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

    sleep(1)

    w_text = browser.find_element(By.CSS_SELECTOR, "h1")
    assert w_text.text == "Congratulations! You have successfully registered!"

finally:
    sleep(10)
    browser.quit()
