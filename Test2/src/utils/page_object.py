# -*- coding:utf-8 -*-
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

import time



class PageObject:
    def __init__(self, driver):
        self.driver = driver
        self.element = None

    def find_element(self,by,value):
        try:
            if by == 'uiautomator':
                self.element = self.driver.find_element_by_android_uiautomator(value)
            elif by == 'xpath':
                self.element = self.driver.find_element_by_xpath(value)
            else:
                pass
        except:
            raise Exception('No such Element')
        return self.element

    def signup_to_login(self, username, pwd):
        '''
        desc:
        :param username:
        :param pwd:
        :return:
        '''
        self.find_element('uiautomator','text(\"Log In\")').click()
        user_add = self.find_element('xpath',
                                     "//*[@resource-id='app']/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View/android.widget.EditText")
        user_add.clear()
        user_add.send_keys(username)
        user_pwd = self.find_element('xpath',
                                    "//*[@resource-id='app']/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.EditText")
        user_pwd.clear()
        user_pwd.send_keys(pwd)
        time.sleep(1)
        self.find_element('xpath',"//*[@resource-id='app']/android.widget.Button").click()


    def button_publish(self):
        element =self.driver.find_element_by_android_uiautomator('text(\"Publish\")')
        return element


    def user_login(self, username, pwd):
        '''
        desc:从主页进去，个人中心的登陆按钮->signup 登陆
        :param username:
        :param pwd:
        :return:
        '''
        self.driver.implicitly_wait(30)
        self.switch_tab('profile')
        # self.find_element('uiautomator','text(\"Log In\")').click()
        self.find_element('uiautomator', 'new UiSelector().textContains("Log")').click()
        self.signup_to_login(username, pwd)

    def switch_tab(self,tab_name):
        '''
        desc:切换到不同菜单
        :param tab_name: 菜单名
        :return:
        '''
        self.driver.implicitly_wait(30)
        if tab_name.lower() == 'profile':
            self.find_element('xpath', "//*[@resource-id='app']/android.view.View[4]/android.view.View[3]").click()
        elif tab_name.lower() == 'home':
            self.find_element('xpath', "//*[@resource-id='app']/android.view.View[4]/android.view.View[1]").click()
        else:
            self.find_element('xpath', "//*[@resource-id='app']/android.view.View[4]/android.view.View[2]").click()

    def select_type(self,type):
        '''
        desc:选择发布一级商品类型
        :param type: 商品类型名称
        :return:
        '''
        _byvalue = None
        if type == 'rent':
            _byvalue = 'new UiSelector().textContains("Rent")'
        elif type == 'job':
            _byvalue = 'new UiSelector().textContains("Jobs")'
        elif type == 'sale':
            _byvalue = 'new UiSelector().textContains("Sale")'
        elif type == 'car':
            _byvalue = 'new UiSelector().textContains("Cars")'
        elif type == 'mobilephone':
            _byvalue = 'new UiSelector().textContains("Mobile")'
        elif type == 'fashion':
            _byvalue = 'new UiSelector().textContains("Fashion")'
        else:
            pass
        self.find_element('uiautomator',type).click()