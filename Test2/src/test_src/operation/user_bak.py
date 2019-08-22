# -*- coding:utf-8 -*-

from src.utils.page_object import PageObject

import time


class Test_user:

    def login(self, driver,userName,userPwd):
        po = PageObject(driver)
        driver.implicitly_wait(30)
        po.find_element('xpath', "//*[@resource-id='app']/android.view.View[4]/android.view.View[3]").click()
        po.find_element('uiautomator', 'text(\"Log In\")').click()
        po.find_element('uiautomator', 'text(\"Log In\")').click()
        # 用户名输入框
        user_add = po.find_element('xpath',
                                   "//*[@resource-id='app']/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View/android.widget.EditText")
        user_add.clear()
        user_add.send_keys(userName)
        # 密码输入框
        user_pwd = po.find_element('xpath',
                                   "//*[@resource-id='app']/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.EditText")
        user_pwd.clear()
        user_pwd.send_keys(userPwd)
        time.sleep(2)
        po.find_element('xpath', "//*[@resource-id='app']/android.widget.Button").click()
        driver.implicitly_wait(10)
        publish_button = po.find_element('uiautomator', 'text(\"Publish\")')
        return publish_button

    def publish(self,driver,test_status):
        pass

