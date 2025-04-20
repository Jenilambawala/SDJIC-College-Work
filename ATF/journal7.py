from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://www.lambdatest.com/selenium-playground/input-form-demo")
print(driver.title)

driver.find_element('id',"name").send_keys("Jenil Ambawala")
time.sleep(1)

driver.find_element('id',"inputEmail4").send_keys("testingjenil@gmail.com")
time.sleep(1)

driver.find_element('id',"inputPassword4").send_keys("Journal@Jenil")
time.sleep(1)

driver.find_element('id',"company").send_keys("JenTech IT Solutions PVT Ltd")
time.sleep(1)

driver.find_element('id',"websitename").send_keys("https://jenilambawala.github.io/MyResume/")
time.sleep(1)

# Select Country
lambdatest = Select(driver.find_element(By.NAME, "country"))
lambdatest.select_by_visible_text("India")
time.sleep(1)

driver.find_element('id',"inputCity").send_keys("Surat")
time.sleep(1)

driver.find_element('id',"inputAddress1").send_keys("Opp Nayara Petrol Pump, Singanpore, Road,")
time.sleep(1)

driver.find_element('id',"inputAddress2").send_keys("Katargam, Surat, Gujarat 395004")
time.sleep(1)

driver.find_element('id',"inputState").send_keys("Gujarat")
time.sleep(1)

driver.find_element('id',"inputZip").send_keys("395004")
time.sleep(5)

# Submit Button
driver.find_element(By.CLASS_NAME, "selenium_btn").click()
time.sleep(10)

driver.close()