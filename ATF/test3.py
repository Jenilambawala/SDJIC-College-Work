from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver .Chrome()
driver.get("https://www.python.org/")
assert "Python" in driver.title

search_bar=driver.find_element(By.NAME, "q")
search_bar.clear()

search_bar.send_keys("sdjic")
search_bar.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

# print("Driver Title", driver.title)
# print("Driver Name", driver.name)
# print("Driver URL", driver.current_url)