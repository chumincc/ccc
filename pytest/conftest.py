# -*- coding:utf-8 -*-
'''
@author:liuchumin
@time:2020/4/1312:49 下午
@desc:
'''
import pytest
from test_case.test_login import test_user_login
import json
from utils.common import get_yaml_data, get_yaml_data_by_keyword, log

env_conf = get_yaml_data('env_conf.yaml')
user = get_yaml_data_by_keyword('post_data.yaml', 'login_user')


@pytest.fixture(scope='session')
def get_token(choose_env):
    try:
        resp_text = test_user_login(user[0], choose_env)
        resp_dict = json.loads(resp_text)
        token = resp_dict['data']['token']
        return token
    except:
        log().error('getToken failed!')
        pytest.xfail('getToken failed!')


def pytest_addoption(parser):
    group = parser.getgroup('chumin_test')
    group.addoption('--env',
                    default='test',
                    dest='--env',
                    help='choose testing environment')


@pytest.fixture(scope='session')
def cmdopt(request):
    env = request.config.getoption('--env', default='test')
    if env in env_conf:
        log().info('---------------------test begins----------------------------')
        log().info('环境：' + env + ',' + env_conf[env])
        return env_conf[env]
    else:
        log().error('此 env 环境不存在，请检查配置参数！')
        pytest.xfail()


@pytest.fixture(scope='session')
def choose_env(cmdopt):
    return cmdopt

# def pytest_gernerate_tests(metafunc):
#     if 'choose_env' in metafunc.fixturenames:
#         metafunc.parametrize('choose_env', scope='function')
