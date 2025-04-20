from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

#inport Action chains

from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object

driver = webdriver.Chrome()

driver.get("https://internshala.com/")

#get element

element = driver.find_element(By.LINK_TEXT, "Register now")

time.sleep(3)

# create action chain object

action = ActionChains(driver)

# Fclick the item

action.click(on_element=element)

action.perform()