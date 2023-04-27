from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time

#set chromodriver.exe path

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.implicitly_wait(0.5)

#launch URL(поиск элемента на странице по XPATH)

driver.get("https://www.rozetka.ua")
elem = driver.find_element(By.XPATH,  '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/div/div/input')
print(elem)
elem.send_keys('samsung')
time.sleep(10)






