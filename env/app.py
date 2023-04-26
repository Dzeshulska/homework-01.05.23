from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

#set chromodriver.exe path

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.implicitly_wait(0.5)

#launch URL

driver.get("https://www.rozetka.ua")

time.sleep(10)

browser = webdriver.Chrome('/path/to/chromedriver')
browser.get('your/website/url')
button = browser.find_element_by_css_selector('button.v-btn.theme--light.primary')
button.click()