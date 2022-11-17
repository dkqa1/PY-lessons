import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/selects1.html")

number_one = driver.find_element(By.ID, "num1")
x = int(number_one.text)

number_two = driver.find_element(By.ID, "num2")
y = int(number_two.text)

a = x + y

print(a)

select = Select(driver.find_element(By.ID, "dropdown"))
select.select_by_value(str(a))

button = driver.find_element(By.TAG_NAME, "button")
button.click()
time.sleep(5)


for num (jekljqwlkjeqwje12[op3p2
])



213123 and




driver.quit()
