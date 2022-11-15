import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
time.sleep(5)

driver.get("https://suninjuly.github.io/math.html")
time.sleep(5)

textarea = driver.find_element(By.CSS_SELECTOR, "#answer")
textarea.send_keys("QWERTY")
time.sleep(1)

checkbox = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
checkbox.click()
time.sleep(1)

radiobutton = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
radiobutton.click()
time.sleep(1)

button = driver.find_element(By.CSS_SELECTOR, "button")
button.click()
time.sleep(10)



driver.quit()
