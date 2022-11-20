from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

driver = webdriver.Chrome()

class test1_do(unittest.TestCase):
    def test_reg1(self):
        driver.get('http://suninjuly.github.io/registration1.html')
        text1 = driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input").send_keys('Denis')
        text2 = driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input").send_keys('Korshunov')
        text3 = driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input").send_keys('test@mail.ru')
        text4 = driver.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input").send_keys('+290-92348')
        text5 = driver.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input").send_keys('Moscow')
        button = driver.find_element(By.TAG_NAME, "button").click()
        text6 = driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", text6)
        time.sleep(10)

    def test_reg2(self):
        driver.get('http://suninjuly.github.io/registration2.html')
        text1 = driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input").send_keys('Denis')
        text2 = driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input").send_keys('Korshunov')
        text3 = driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input").send_keys('test@mail.ru')
        text4 = driver.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input").send_keys('+290-92348')
        text5 = driver.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input").send_keys('Moscow')
        button = driver.find_element(By.TAG_NAME, "button").click()
        text6 = driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", text6)



if __name__ == "__main__":
    unittest.main()
