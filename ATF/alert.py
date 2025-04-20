from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://pythonbasics.org/")
js = 'alert("Hello World")'
driver.execute_script(js)
time.sleep(4)