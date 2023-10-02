from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"


try:
    browser.get(link)
    btn = browser.find_element(By.CLASS_NAME, 'btn').click()
    acceptALERT = browser.switch_to.alert
    acceptALERT.accept()

    getNumber = browser.find_element(By.ID, 'input_value').text
    answer = browser.find_element(By.ID,'answer').send_keys(calc(getNumber))
    sbtBtn = browser.find_element(By.CLASS_NAME, 'btn').click()



finally:
    time.sleep(20)
    browser.quit()



