from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    # link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    firstName = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first')
    firstName.send_keys("123")

    lastName = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.second')
    lastName.send_keys("321")

    emailField = browser.find_element(By.CSS_SELECTOR, 'input.third')
    emailField.send_keys('test@mail.com')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()