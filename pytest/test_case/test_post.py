# -*- coding:utf-8 -*-
'''
@author:liuchumin
@time:2020/4/1311:29 上午
@desc:
'''
import pytest
from utils.common import assertion, post_request, get_yaml_data_by_keyword, post_data_preload


class TestPost:
    post_data = get_yaml_data_by_keyword('post_data.yaml', 'post_data')

    @pytest.fixture(params=post_data)
    def test_post_data(self, request, get_token):
        if get_token:
            data = post_data_preload(request.param, get_token)
            return data

    def test_post(self, test_post_data, choose_env):
        response = post_request(test_post_data, choose_env)
        assertion(response)

