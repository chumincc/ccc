# -*- coding:utf-8 -*-

import pytest
import src.test_src.operation.user_bak as user
from data import fix_data
from src.utils.common import check_point

user = user.Test_user()
test_login_data = [(fix_data.seller_phone, fix_data.seller_password)]
res = None

@pytest.mark.parametrize( 'username, userpwd', test_login_data)
def test_login(get_driver, username, userpwd):
    res = user.login(get_driver, username, userpwd)
    check_point(res)


def test_publish():
    pass