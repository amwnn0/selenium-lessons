import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link1 = 'https://suninjuly.github.io/registration1.html'
link2 = 'https://suninjuly.github.io/registration2.html'
congrats = 'Congratulations! You have successfully registered!'


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Chrome()
        browser.get(link1)
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys('John')
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys('Test')
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('email@email.com')
        browser.find_element(By.CSS_SELECTOR, 'button').click()
        # WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h1'), congrats))
        self.assertEqual(browser.find_element(By.CSS_SELECTOR, 'h1').text, congrats, "test1 failed")

    def test_abs2(self):
        browser = webdriver.Chrome()
        browser.get(link2)
        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('John')
        browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('email@<EMAIL>')
        browser.find_element(By.CSS_SELECTOR, 'button').click()
        # WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h1'), congrats))
        self.assertEqual(browser.find_element(By.CSS_SELECTOR, 'h1').text, congrats, "test1 failed")


if __name__ == '__main__':
    unittest.main()
