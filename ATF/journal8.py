import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")

# Sample Web Page To Test

driver.find_element('name', "username").send_keys("Jenil Ambawala")
time.sleep(1)

driver.switch_to.default_content()

driver.find_element('name', "password").send_keys("Journal@Jenil")
time.sleep(1)

driver.find_element('name', "comments").send_keys("Jenil Ambawala Automation Testing")
time.sleep(1)

# Checkbox
driver.find_element(By.XPATH, "//input[@value='cbselenium']").click()
time.sleep(1)

# Radio Button
driver.find_element('name', "radioselenium").click()
time.sleep(1)

# Multiple Select Values
hobbies = Select(driver.find_element(By.NAME, "multipleselect[]"))
hobbies.select_by_visible_text("Selenium")
hobbies.select_by_visible_text("Performance Testing")

# Dropdown
lambdatest = Select(driver.find_element(By.NAME, "dropdown"))
lambdatest.select_by_value('ddselenium')
time.sleep(2)

# Date Picker
driver.find_element(By.NAME, 'bday').send_keys("10-11-2002")
time.sleep(3)

# Upload File
file_input = driver.find_element(By.NAME, "filename")
file_path = "E:/SDJIC/Work/ATF/jenilmywp.png "
file_input.send_keys(file_path)
time.sleep(3)

# Download FIle
driver.find_element(By.LINK_TEXT, "Download CSV File").click()
time.sleep(3)

# Select Table
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'spTable')))
employee_name = "Employee 2"
rows = driver.find_elements(By.XPATH, "//table[@class='spTable']//tr[@class='spTableTr']")

for row in rows:
    # Check if the row contains the employee name
    if employee_name in row.text:
        # Locate the radio button in the same row and click it
        radio_button = row.find_element(By.XPATH, ".//input[@type='radio']")
        radio_button.click()

time.sleep(3)

# Button Click
driver.find_element('name', "spbutton").click()
time.sleep(3)

# Leave a Reply Form

# textarea => comment
driver.find_element('id', "comment").send_keys("Jenil Ambawala is on 2 days Leave from Personal Reason.")
time.sleep(1)

# Name
driver.find_element('id', "author").send_keys("Jenil Ambawala")
time.sleep(1)

# Mail
driver.find_element('id', "email").send_keys("testing.jenil@gmail.com")
time.sleep(1)

# Website
driver.find_element('id', "url").send_keys("https://jenilambawala.github.io/MyResume/")
time.sleep(1)

# Submit
driver.find_element('id', "submit").click()
time.sleep(10)

driver.close() 