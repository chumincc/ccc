# -*- coding:utf-8 -*-

import pytest

import src.operation.user as user

from data import fix_data
from src.utils.common import check_point



class Test_user:
    test_login_data = [(fix_data.seller_phone, fix_data.seller_password)]

    @pytest.mark.parametrize('username, userpwd', test_login_data)
    def test_login(self,get_driver,username, userpwd):
        self.res = user.userLogin(get_driver, username, userpwd)
        check_point(self.res)



