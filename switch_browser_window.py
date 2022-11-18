import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/redirect_accept.html')

button_ = driver.find_element(By.TAG_NAME, 'button').click()

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

number = driver.find_element(By.ID,'input_value').text
x = number
y = calc(x)

answer = driver.find_element(By.ID, 'answer').send_keys(y)

submit = driver.find_element(By.TAG_NAME, 'button').click()
time.sleep(5)

driver.quit()
