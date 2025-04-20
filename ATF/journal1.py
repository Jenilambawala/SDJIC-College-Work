from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

driver.find_element('id',"APjFqb").send_keys("Selenium Testing")
time.sleep(2)

driver.find_element('id',"APjFqb").send_keys(Keys.ENTER)
time.sleep(2)

driver.close()