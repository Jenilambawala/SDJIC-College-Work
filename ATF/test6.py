from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

# driver.get("https://www.indeed.jobs/")
# print(driver.title)
# driver.find_element('id',"location-select").send_keys("India")
# time.sleep(3)
# driver.find_element('type',"button").send_keys(Keys.ENTER)
# print(driver.current_url)
# time.sleep(10)
# driver.close()


# driver = webdriver.Chrome()

driver.get("https://www.indeed.jobs/")
print(driver.title)
driver.find_element('id',"location-select").send_keys("India")
time.sleep(3)
driver.find_element('id',"button").send_keys(Keys.ENTER)
print(driver.current_url)
time.sleep(10)
driver.close()