from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://autopract.com/selenium/upload1/")
file_input = driver.find_element(By.NAME, "files[]")
file_path = "E:/SDJIC/Work/ATF/jenilmywp.png"
file_input.send_keys(file_path)

time.sleep(2)

driver.find_element(By.CLASS_NAME, "start").click()
time.sleep(3)

print(driver.find_element(By.CLASS_NAME, "name").text)
time.sleep(10)

driver.close()