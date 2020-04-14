# -*- coding:utf-8 -*-
import configparser
import os
import time
import traceback



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
    # print(attr)
    return attr

# 检查点
def check_point(element):
    assert element != None


# 生成日期
def current_date():
    '''生成当前日期字符串'''
    date = time.localtime()
    return '-'.join([str(date.tm_year), str(date.tm_mon), str(date.tm_mday)])


def current_time():
    '''生成当前时间字符串'''
    date = time.localtime()
    return str(date.tm_hour),''.join([str(date.tm_hour), str(date.tm_min), str(date.tm_sec)])


def create_dir(dir_name):
    '''创建当前日期和当前时间目录,dir_name为根目录下的二级目录名'''
    path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    date_dir = os.path.join(path,dir_name,current_date())
    if not os.path.exists(date_dir):
        os.mkdir(date_dir)
    time_dir = os.path.join(date_dir, current_time()[0])
    if not os.path.exists(time_dir):
        os.mkdir(time_dir)
    return time_dir




# if __name__ == '__main__':
#     create_dir('report')