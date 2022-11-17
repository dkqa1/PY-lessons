import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
time.sleep(1)

driver.get("http://suninjuly.github.io/get_attribute.html")
time.sleep(5)

x_element = driver.find_element(By.ID, "treasure")
number = x_element.get_attribute('valuex')
x = number
y = calc(x)

textarea = driver.find_element(By.CSS_SELECTOR, "#answer")
textarea.send_keys(y)
time.sleep(1)

checkbox = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
checkbox.click()
time.sleep(1)

radiobutton = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
radiobutton.click()
time.sleep(1)

button = driver.find_element(By.TAG_NAME, "button")
button.click()
time.sleep(5)

driver.quit()
