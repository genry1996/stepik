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
    # 1) Открываем страницу
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # 2) Ждём, пока в элементе с ценой появится "$100"
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 3) Нажимаем кнопку Book
    browser.find_element(By.ID, "book").click()

    # 4) Считываем x
    x = browser.find_element(By.ID, "input_value").text

    # 5) Считаем ответ по формуле
    y = calc(x)

    # 6) Вводим ответ
    browser.find_element(By.ID, "answer").send_keys(y)

    # 7) Нажимаем Submit
    browser.find_element(By.ID, "solve").click()

    # 8) Забираем число из alert
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    print("CODE:", alert.text)
    alert.accept()

finally:
        time.sleep(2)
        browser.quit()
