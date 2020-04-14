# -*- coding:utf-8 -*-
'''
@author:liuchumin
@time:2020/4/1311:29 上午
@desc:
'''
from data import post_data, data_preload
import pytest
from utils.common import assertion, post_request


class TestPost():

    @pytest.fixture(params=post_data.post_data)
    def test_post_data(self, request, get_token):
        data=data_preload.post_data_preload(request.param,get_token)
        return data

    def test_post(self, test_post_data):
        response = post_request(test_post_data)
        assertion(response)

