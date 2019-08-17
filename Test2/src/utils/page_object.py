# -*- coding:utf-8 -*-
from appium import webdriver

import time


class UserPageObject:
    def __init__(self, driver):
        self.driver = driver

    def signup_to_login(self, username, pwd):
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
        return element

    def user_login(self, username, pwd):
        self.driver.find_element_by_android_uiautomator('text(\"Log In\")')
        self.signup_to_login(username, pwd)
