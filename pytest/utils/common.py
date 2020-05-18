# -*- coding:utf-8 -*-
'''
@author:liuchumin
@time:2020/4/129:56 下午
@desc:
'''

import logging
import json
import os
import time
from logging.handlers import TimedRotatingFileHandler
import requests
from requests import RequestException
import yaml

format_time = time.strftime('%Y%m%d%H%M', time.localtime())
project_dir = os.path.join(os.path.abspath(os.path.dirname(__file__).split('pytest')[0]), 'pytest/')


def assertion(response, exp_code=200):
    '''封装断言'''
    if response is not None:
        assert response.status_code == exp_code
        dict_resp = json.loads(response.text)
        assert dict_resp.get('data', False)
    else:
        log().error('No response!')
        raise AssertionError


def log(*message):
    '''打印日志'''
    logger = logging.getLogger(__name__)
    if not logger.handlers:
        log_path = os.path.join(project_dir, 'log/')
        # std_time = time.strftime('%Y%m%d', time.localtime())
        print(log_path)
        logfile = log_path + 'all'
        print(logfile)
        logger.setLevel(level=logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
        handler = TimedRotatingFileHandler(filename=logfile, when='M', interval=1, backupCount=3)
        handler.suffix = "%Y-%m-%d_%H-%M.log"
        handler.setFormatter(formatter)
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(handler)
        logger.addHandler(console)
    return logger
    # logger.info(message)


def get_token(resp_text):
    '''从response_text中，获取token'''
    resp_dict = json.loads(resp_text)
    token = resp_dict['data']['token']
    return token


def post_request(post_dict, url):
    '''
    公共post请求
    :param post_dict: 请求的所有数据
    :param url: 请求的域名
    :return:
    '''
    comment = post_dict['comment']
    path = post_dict['path']
    headers = post_dict['header']
    body = json.dumps(post_dict['body'])
    path = url + path
    log().info('comment= ' + comment + ', path= ' + path + ', headers= ' + str(headers) + ', body= ' + str(body))
    try:
        response = requests.post(url=path, data=body, headers=headers)
        log().info("response= " + str(response.status_code) + str(response.text))
        return response
    except RequestException:
        log().error('ERROR：bad request！')
        raise Exception('错误的请求！！')


def get_yaml_data(path):
    '''
    获取yaml中的数据
    :param path: 请求文件名
    :return: 返回全部数据
    '''
    path = os.path.join(project_dir, 'data/', path)
    with open(path, 'r') as f:
        test_data = yaml.load(f)
    return test_data


def get_yaml_data_by_keyword(path, keyword):
    '''
    获取yaml中的数据
    :param path: 请求文件名
    :return: 返回关键字的数据
    '''
    path = os.path.join(project_dir, 'data/', path)
    with open(path, 'r') as f:
        test_data = yaml.load(f)
    return test_data[keyword]


def post_data_preload(post_data, token, *kwgs):
    '''
    post中的token替换
    :param post_data:
    :param token:
    :param kwgs:
    :return:
    '''
    post_data['header']['X-HEAD-AUTH-TOKEN'] = token
    return post_data


if __name__ == '__main__':
    pass
