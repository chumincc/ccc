from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
path = os.path.dirname("__file__")
time.sleep(3)
driver.get_screenshot_as_file(path+"screenshot_web.png")
driver.close()

