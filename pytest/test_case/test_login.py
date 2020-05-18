# -*- coding:utf-8 -*-
'''
@author:liuchumin
@time:2020/4/1210:19 下午
@desc:
'''

import pytest
from utils.common import assertion, post_request, get_yaml_data_by_keyword

user = get_yaml_data_by_keyword('post_data.yaml', 'login_user')


@pytest.fixture(params=user)
def test_get_user(request):
    return request.param


def test_user_login(test_get_user, choose_env):
    response = post_request(test_get_user, choose_env)
    assertion(response)
    return response.text
