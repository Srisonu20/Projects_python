import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("https://paint-studio.netlify.app/#")
time.sleep(2)
menu = driver.find_element(By.XPATH,"//img[@id='menu']")
menu.click()
time.sleep(2)

hover = driver.find_element(By.XPATH,"//body/section[@id='banner']/div[1]/div[1]/a[1]/span[1]")
actions = ActionChains(driver)
actions.move_to_element(hover).perform()
time.sleep(3)

driver.execute_script("window.scrollBy(0,500)","")
time.sleep(3)






