from src.utils import page_object
from appium import webdriver



def userLogin(driver,username,pwd):
    user = page_object.UserPageObject(driver)
    user.user_login(username,pwd)
