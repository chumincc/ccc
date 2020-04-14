#-*- coding:utf-8 -*-
'''
@author:liuchumin
@time:2019/9/510:51 上午
@desc:
'''

from src.utils import page_object

def postCar(driver):
    po = page_object.PageObject(driver)
    po.switch_tab('post')
    po.select_type('cars')