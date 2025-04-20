from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.geeksforgeeks.org/")

driver.refresh()

a = ActionChains(driver)

a.key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()

driver.close()