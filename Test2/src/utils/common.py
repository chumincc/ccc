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
    print(attr)
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
    return ''.join([str(date.tm_hour), str(date.tm_min), str(date.tm_sec)])


def create_dir(dir_name):
    '''创建当前日期和当前时间目录'''
    path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    date_dir = os.path.join(path,dir_name,current_date())
    if not os.path.exists(date_dir):
        os.mkdir(date_dir)
    time_dir = os.path.join(date_dir, current_time())
    if not os.path.exists(time_dir):
        os.mkdir(time_dir)
    return time_dir


# 截图
def screenshot(driver,pictureName):
    '''
    desc:生成截图
    :param driver:
    :param pictureName: 调用的方法/函数名
    :return:
    '''
    picturePath = os.path.join(create_dir(), pictureName+'.png')
    try:
        driver.get_screenshot_as_file(picturePath)
    except Exception  as e:
        print(traceback.print_exc())

# if __name__ == '__main__':
#     create_dir('report')