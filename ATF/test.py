from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.co.in/")
print("Driver Title", driver.title)
print("Driver Name", driver.name)
print("Driver URL", driver.current_url)