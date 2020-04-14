from src.utils import page_object


def userLogin(driver,username,pwd):
    '''desc:主页用户登陆'''
    po = page_object.PageObject(driver)
    po.user_login(username,pwd)
    return po.button_publish()



