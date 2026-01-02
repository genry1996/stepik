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
    # 1) Открываем первую страницу
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # 2) Запоминаем текущую вкладку (до клика)
    first_window = browser.current_window_handle

    # 3) Нажимаем кнопку, которая откроет новую вкладку
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 4) Ждём, пока вкладок станет 2
    WebDriverWait(browser, 10).until(EC.number_of_windows_to_be(2))

    # 5) Берём ID новой вкладки и переключаемся на неё
    new_window = [w for w in browser.window_handles if w != first_window][0]
    browser.switch_to.window(new_window)

    # 6) Читаем x на новой вкладке
    x = browser.find_element(By.ID, "input_value").text

    # 7) Считаем y
    y = calc(x)

    # 8) Вводим ответ
    browser.find_element(By.ID, "answer").send_keys(y)

    # 9) Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 10) Забираем код из alert
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    print("CODE:", alert.text)
    alert.accept()

    time.sleep(2)

finally:
    browser.quit()
