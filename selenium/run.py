import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/ref=nav_logo")
time.sleep(3)
driver.find_element(By.XPATH,"//a[@id='nav-hamburger-menu']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//body/div[@id='hmenu-container']/div[@id='hmenu-canvas-background']/div[1]").click()

time.sleep(2)
driver.quit()