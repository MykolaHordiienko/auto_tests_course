# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# # def calc(x):
# #     return str(math.log(abs(12*math.sin(int(x)))))
#
# browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/wait1.html"
#
# try:
#     browser.get(link)
#     verifyBtn = browser.find_element(By.ID, 'verify').click()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # import time
#
# browser = webdriver.Chrome()
# # browser.implicitly_wait(5)
# browser.get("http://suninjuly.github.io/cats.html")
# btn = browser.find_element(By.ID, "button")


# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text