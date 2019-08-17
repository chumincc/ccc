from src.utils import page_object
from appium import webdriver

class
user=page_object.UserPageObject(driver)
def userLogin(username,pwd):
    user.user_login(username,pwd)
