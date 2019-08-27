# -*- coding:utf-8 -*-
from appium import webdriver
<<<<<<< HEAD
import time
=======
>>>>>>> 7a2e6fbb7536dd8ee3ebf0ad3b2158f670a3bd16


class PageObject:
    def __init__(self,driver):
        self.driver = driver

    # 查找页面元素
    def find_element(self, by, by_value):
        element = None
        if by == 'xpath':
            element = self.driver.find_element_by_xpath(by_value)
        elif by == 'uiautomator':
            element = self.driver.find_element_by_android_uiautomator(by_value)
        else:
            pass
        return element

<<<<<<< HEAD
class User:
    def __init__(self,driver):
        self.driver = driver

    def signupToLogin(self,username,pwd):
        self.driver.find_element_by_android_uiautomator('text(\"Log In\")')
        user_add = self.driver.find_element_by_xpath('xpath',
                                   "//*[@resource-id='app']/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View/android.widget.EditText")

        user_add.clear()
        user_add.send_keys(username)
        # 密码输入框
        user_pwd = self.driver.find_element_by_xpath('xpath',
                                   "//*[@resource-id='app']/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.EditText")
        user_pwd.clear()
        user_pwd.send_keys(pwd)
        time.sleep(1)
        self.driver.find_element_by_xpath('xpath', "//*[@resource-id='app']/android.widget.Button").click()

    def button_publish(self):
        element = self.driver.find_element_by_android_uiautomator('text(\"Publish\")')
        return  element

    def user_login(self,username,pwd):
        self.driver.find_element_by_android_uiautomator('text(\"Log In\")')
        self.signupToLogin(username,pwd)
=======

>>>>>>> 7a2e6fbb7536dd8ee3ebf0ad3b2158f670a3bd16

