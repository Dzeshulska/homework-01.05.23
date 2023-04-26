from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time

#set chromodriver.exe path

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.implicitly_wait(0.5)

#launch URL

driver.get("https://www.rozetka.ua")

time.sleep(10)

text_input = driver.find_element(By.ID, "textInput")
ActionChains(driver)\
      .send_keys_to_element(text_input, "samsung")\
      .perform()

time.sleep(20)
