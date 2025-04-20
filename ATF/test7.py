from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

journalAddress = "https://www.federalregister.gov/documents/2024/06/24/2024-13188/removal-of-affirmative-defense-provisions-from-specified-new-source-performance-standards-and"

driver.get(journalAddress)

time.sleep(2)

articleObjects = driver.find_elements(By.XPATH,'//div[@id="fulltext_content_area"]/*')

articleDictionary = dict()

myKey = ""

myValue_total = ""

for i in range(len(articleObjects)):
    tagName = articleObjects[i].tag_name

    if tagName.startswith("h"):

        if myKey:

            articleDictionary[myKey] = myValue_total

            myKey = ""

            myValue_total = ""

        myKey = articleObjects[i].get_attribute("innerText")

    if tagName.startswith("p"):

        myValue = articleObjects[i].get_attribute("innerText") 
        myValue_total = myValue_total + myValue

    if tagName.startswith("ul"):

        myBullets = articleObjects[i].find_elements (By. XPATH,'li') 

        for j in range(len(myBullets)): 

            myBullet = myBullets[j].get_attribute("innerText")

            myValue_total = myValue_total + myBullet

driver.close()

article = ''
for key, value in articleDictionary.items():

     article = article + key + '\n\n' + value + '\n\n************\n\n'

print(article)
