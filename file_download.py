from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)
    #Fill the data
    name = browser.find_element(By.NAME, 'firstname').send_keys('SomeName')
    # name.send_keys('SomeName')
    lastName = browser.find_element(By.NAME, 'lastname').send_keys('TestLastName')
    # lastName.send_keys('TestLastName')
    mailField = browser.find_element(By.NAME, 'email').send_keys("test@email.com")
    # mailField.send_keys("test@email.com")

    # fileBtn = browser.find_element(By.ID, 'file').click()

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.ID, 'file').send_keys(file_path)
    # element.send_keys(file_path)

    submitBtn = browser.find_element(By.CLASS_NAME, 'btn').click()
finally:
    time.sleep(30)
    browser.quit()
