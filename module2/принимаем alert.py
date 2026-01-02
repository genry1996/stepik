from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
try:
    # 1) открываем страницу
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # 2) жмём кнопку
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 3) принимаем confirm (OK)
    confirm = WebDriverWait(browser, 10).until(EC.alert_is_present())
    confirm.accept()

    # 4) на новой странице читаем x
    x = browser.find_element(By.ID, "input_value").text

    # 5) считаем ответ
    y = calc(x)

    # 6) вводим ответ
    browser.find_element(By.ID, "answer").send_keys(y)

    # 7) отправляем
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 8) забираем код из alert и печатаем
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    print("CODE:", alert.text)
    alert.accept()

    time.sleep(2)

finally:
    browser.quit()
