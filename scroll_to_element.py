import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

#Функция
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Запуск браузера
driver = webdriver.Chrome()

#Переход на страницу
driver.get("http://suninjuly.github.io/execute_script.html")

#Поиск значения
x_element = driver.find_element(By.ID, "input_value")
number = x_element.text
x = number
y = calc(x)

#Поиск и передача значения в форму ответа
textarea = driver.find_element(By.CSS_SELECTOR, "#answer")
textarea.send_keys(y)
time.sleep(1)

#Поиск кнопки и скролл
button = driver.find_element(By.TAG_NAME, "button")
driver.execute_script("arguments[0].scrollIntoView(true);", button)

#Выбора чекбокса
checkbox = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
checkbox.click()

#Выбор радиобаттона
radiobutton = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
radiobutton.click()

#Нажатие кнопки
button.click()
time.sleep(5)

driver.quit()
