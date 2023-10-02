from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/selects2.html"

try:
    browser.get(link)
    firstNum = browser.find_element(By.ID, 'num1').text
    secondNum = browser.find_element(By.ID, 'num2').text
    sumOfNumbers = str(int(firstNum) + int(secondNum))

    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, f"[value='{sumOfNumbers}']").click()
    # more easier way
    # select = Select(browser.find_element(By.TAG_NAME, "select"))
    # select.select_by_value(sumOfNumbers)

    submitBtn = browser.find_element(By.CLASS_NAME, "btn.btn-default").click()

finally:
    time.sleep(30)
    browser.quit()
