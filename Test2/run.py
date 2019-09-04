#-*- coding: UTF-8 -*-
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
print ('11111')
driver.quit()
