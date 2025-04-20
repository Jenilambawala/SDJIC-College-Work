from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://internshala.com/")
driver.maximize_window()
source_element = driver.find_element(By.LINK_TEXT,"Register now")

target_element = driver.find_element(By.LINK_TEXT,"Candidate Sign-up")

action =  ActionChains(driver)

# click,double_click,click_and_hold,
action.drag_and_drop(source_element,target_element)

action.perform()