# -*- coding:utf-8 -*-
'''
@author:liuchumin
@time:2020/4/1210:19 下午
@desc:
'''

import pytest
from utils.common import assertion, post_request
from data import user


@pytest.fixture(params=user.user)
def test_get_user(request):
    return request.param


def test_user_login(test_get_user):
    response = post_request(test_get_user)
    assertion(response)
    return response.text
