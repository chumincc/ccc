from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
driver.get("https://honeycomb.xgo.city/1.1.0/#/")
path = os.path.dirname("__file__")
time.sleep(3)
driver.maximize_window()
driver.get_screenshot_as_file(path+"9.png")
driver.quit()

