# -*- coding:utf-8 -*-

import pytest
<<<<<<< HEAD
import src.test_src.operation.user_bak as user
=======
import src.test_src.test_common.user as user
>>>>>>> 7a2e6fbb7536dd8ee3ebf0ad3b2158f670a3bd16
from data import fix_data
from src.utils.common import check_point

user = user.Test_user()
test_login_data = [(fix_data.seller_phone, fix_data.seller_password)]
res = None

@pytest.mark.parametrize( 'username, userpwd', test_login_data)
def test_login(get_driver, username, userpwd):
    res = user.login(get_driver, username, userpwd)
    check_point(res)


<<<<<<< HEAD
def test_publish():
    pass
=======
>>>>>>> 7a2e6fbb7536dd8ee3ebf0ad3b2158f670a3bd16
