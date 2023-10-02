from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(x))
    checkbox = browser.find_element(By.ID, 'robotCheckbox').click()
    radioBtn = browser.find_element(By.ID, 'robotsRule')
    radioBtn.location_once_scrolled_into_view
    radioBtn.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.location_once_scrolled_into_view
    button.click()

finally:
    time.sleep(30)
    browser.quit()
