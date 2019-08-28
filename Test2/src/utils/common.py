# -*- coding:utf-8 -*-
import configparser
import os


# 获取配置
def get_config(sector):
    conf = configparser.RawConfigParser()
    path = os.path.join(os.path.dirname((os.path.dirname(os.path.dirname(os.path.abspath(__file__))))),'data','test_data.ini')
    conf.read(path, encoding='utf-8')
    confs = conf.items(sector)
    dict_confs = dict(confs)
    return dict_confs


# 获取连接配置
def startup_conf():
    conf = get_config('phone_1')
    attr = {
        "appPackage": conf['apppackage'],
        "appActivity": conf['appactivity'],
        "platformVersion": conf['platformversion'],
        "platformName": conf['platformname'],
        "deviceName": conf['devicename'],
        "newCommandTimeout": conf['newcommandtimeout'],
        "noReset": conf['noreset'],
        "unicodeKeyboard": conf['unicodekeyboard'],
        "clearSystemFiles": conf['clearsystemfiles'],
        "automationName": conf['automationname']
    }
    print(attr)
    return attr

# 检查点
def check_point(element):
    assert element != None

# 截图
def screenshot():
    pass
