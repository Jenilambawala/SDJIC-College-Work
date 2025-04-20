from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://www.browserstack.com/")

element = driver.find_element("link text", "Sign in")

action = ActionChains(driver)

action.click(on_element = element)

action.perform()