import time
# import outlook
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#driver = webdriver.Firefox()
driver = webdriver.Chrome("/home/esteban/UTEC/chromedriver")
driver.get("https://ev1.utec.edu.uy/moodle/")
elemento1 = driver.find_element(By.ID, "inputName")
elemento1.clear()
elemento1.send_keys("esteban.martinez")

elemento2 = driver.find_element(By.ID, "inputPassword")
elemento2.clear()
elemento2.send_keys("T3.14yxakutec")

driver.find_element(By.ID, "submit").click()
time.sleep(20)

driver.find_element(By.PARTIAL_LINK_TEXT, 'Taller Devops_OCTAVO SEMESTRE DZ').click()


time.sleep(20)

driver.close()