# -*- coding:utf-8 -*-
'''
@author:liuchumin
@time:2020/4/265:49 下午
@desc:
'''
import pytest

if __name__ == '__main__':
    pytest.main(['-s','--alluredir=./allure-results ','--env=test','./test_post/test_login.py'])
    # pytest.main('')

