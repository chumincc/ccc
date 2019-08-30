from src.utils import page_object
from appium import webdriver



def userLogin(driver,username,pwd):
    '''
    desc:主页用户登陆
    :param driver:
    :param username:
    :param pwd:
    :return:
    '''
    user = page_object.UserPageObject(driver)
    user.user_login(username,pwd)
    return user.button_publish()
