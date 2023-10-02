from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser.get(link)
    btnFirstPage = browser.find_element(By.CLASS_NAME, 'trollface').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value').text
    answer = browser.find_element(By.ID, 'answer').send_keys(calc(x))
    submit = browser.find_element(By.CLASS_NAME, 'solve').click()

    # current_window = browser.current_window_handle

finally:

    time.sleep(20)
    browser.quit()