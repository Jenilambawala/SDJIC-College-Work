from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("https://www.federalregister.gov/documents/2013/09/24/2013-21228/affirmative-action-andnondiscrimination-obligations-of-contractors-and-subcontractors-regarding")

# Wait for the "Search" button to be clickable
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "search-button"))
)

# Click the "Search" button
search_button.click()

# Wait for the search results to be loaded
search_results = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".search-result"))
)

# Print the number of search results
print(f"Found {len(search_results)} search results")

# Close the browser
driver.quit()