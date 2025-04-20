from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get("https://www.irctc.co.in/nget/profile/user-registration")
print(driver.title)

driver.find_element('id',"userName").send_keys("devyanshu")
time.sleep(3)

driver.find_element('id',"usrPwd").send_keys("Devyanshu@123")
time.sleep(3)

driver.find_element('id',"cnfUsrPwd").send_keys("Devyanshu@123")
time.sleep(3)


# driver.find_element('id',"continue-announce").send_keys(Keys.ENTER)
# print(driver.current_url)
# time.sleep(10)
# driver.close()