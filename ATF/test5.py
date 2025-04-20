from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

# driver.get("https://www.indeed.jobs/")
# print(driver.title)
# driver.find_element('id',"location-select").send_keys("India")
# time.sleep(3)
# driver.find_element('type',"button").send_keys(Keys.ENTER)
# print(driver.current_url)
# time.sleep(10)
# driver.close()


driver = webdriver.Chrome()

driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Ftag%3Dmsndeskstdin-21%26ref%3Dnav_ya_signin%26adgrpid%3D1328211703591630%26hvadid%3D83013495293827%26hvnetw%3Do%26hvqmt%3De%26hvbmt%3Dbe%26hvdev%3Dc%26hvlocint%3D%26hvlocphy%3D149053%26hvtargid%3Dkwd-83014163717471%3Aloc-90%26hydadcr%3D5621_2377279%26msclkid%3D458de512f9521989d20c83a2b67e0afb&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
print(driver.title)
driver.find_element('id',"ap_email").send_keys("6351644181")
time.sleep(3)
driver.find_element('id',"continue-announce").send_keys(Keys.ENTER)
print(driver.current_url)
time.sleep(10)
driver.close()