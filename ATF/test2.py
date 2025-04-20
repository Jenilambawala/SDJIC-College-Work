from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.python.org/")
driver.find_element('id',"id-search-field").send_keys("Download")
time.sleep(3)
driver.find_element('name',"submit").send_keys(Keys.RETURN)
time.sleep(3)
print(driver.current_url)
driver.close()

# print("Driver Title", driver.title)
# print("Driver Name", driver.name)
# print("Driver URL", driver.current_url)