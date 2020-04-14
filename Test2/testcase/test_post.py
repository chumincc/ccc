# -*- coding:utf-8 -*-

import pytest

import src.operation.post as post

from src.utils.common import check_point

class Test_post:

    def test_post_car(self,get_driver):
        self.res = post.postCar(get_driver)
        check_point(self.res)