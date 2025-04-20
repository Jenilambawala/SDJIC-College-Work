from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/accounts/login/?hl=en")
print(driver.title)
driver.find_element('name',"username").send_keys("div.yanshu_07")

# driver.find_element('aria-label',"Password").send_keys("08102003oct")
time.sleep(3)
driver.find_element('type',"submit").send_keys(Keys.ENTER)
print(driver.current_url)
time.sleep(10)
driver.close()