import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button = driver.find_element(By.ID, "book").click()

number = driver.find_element(By.ID,'input_value').text
x = number
y = calc(x)

select = driver.find_element(By.ID, "solve")
driver.execute_script("arguments[0].scrollIntoView(true);", select)

answer = driver.find_element(By.ID, 'answer').send_keys(y)

select.click()

time.sleep(5)

driver.quit()
