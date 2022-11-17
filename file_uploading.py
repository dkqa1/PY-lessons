import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


#Запуск браузера
driver = webdriver.Chrome()

#Переход на страницу
driver.get("http://suninjuly.github.io/file_input.html")

#Поиск и передача значения в форму ответов: Имя, Фамилия, Почта
form_name = driver.find_element(By.NAME, "firstname").send_keys('John')

form_surname = driver.find_element(By.NAME, "lastname").send_keys('Wick')

mail = driver.find_element(By.NAME, "email").send_keys('test@gmail.com')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'textfile.txt')
upload_button = driver.find_element(By.ID, 'file')
upload_button.send_keys(file_path)

#Поиск и Нажатие кнопки
button = driver.find_element(By.TAG_NAME, 'button').click()
time.sleep(5)

driver.quit()
