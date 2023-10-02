from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

link = ('http://suninjuly.github.io/explicit_wait2.html')

try:
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    # '$100'
    # price = browser.find_element(By.ID, 'price')
    bookBtn = browser.find_element(By.ID, 'book').click()


    x = browser.find_element(By.ID, 'input_value').text
    answer = browser.find_element(By.ID, 'answer')
    answer.location_once_scrolled_into_view
    answer.send_keys(calc(x))
    submit = browser.find_element(By.ID, 'solve').click()
finally:
    time.sleep(20)
    browser.quit()

