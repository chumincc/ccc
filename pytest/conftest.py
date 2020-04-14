#-*- coding:utf-8 -*-
'''
@author:liuchumin
@time:2020/4/1312:49 下午
@desc:
'''
import pytest
from test_case.test_login import test_user_login
from data.user import user
import json


@pytest.fixture(scope='session')
def get_token():
    resp_text = test_user_login(user[0])
    resp_dict = json.loads(resp_text)
    token = resp_dict['data']['token']
    return token

