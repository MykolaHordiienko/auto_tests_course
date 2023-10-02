from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

try:
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")


   # x_element = browser.find_element(By.ID, 'input_value')
    treasure = browser.find_element(By.ID, 'treasure')
    x_elem = treasure.get_attribute("valuex")
    print('value x = ', x_elem)
    # x = x_elem.text
    y = calc(x_elem)

    # Write result to the field

    textField = browser.find_element(By.ID, 'answer')
    textField.send_keys(y)

    # checked "I'm the robot"

    checkBox = browser.find_element(By.ID, 'robotCheckbox')
    checkBox.click()
    # Verified checkbox by default
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is selected by default"
    # the same as above assert people_checked == "true", "People radio is not selected by default"
    # Select another checkbox

    radioBtn = browser.find_element(By.ID, 'robotsRule')
    robots_checked = radioBtn.get_attribute("checked")
    print("value of Robot radio: ", robots_checked)
    assert robots_checked is None, "The Robot radiobutton isn`t checked"
    radioBtn.click()

    submitBtn = browser.find_element(By.CLASS_NAME, 'btn-default')
    submitBtn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()