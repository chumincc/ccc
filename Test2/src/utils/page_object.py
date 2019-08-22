# -*- coding:utf-8 -*-
from appium import webdriver


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



