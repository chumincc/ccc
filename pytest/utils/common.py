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
import requests
from data import global_conf

format_time = time.strftime('%Y%m%d%H%M', time.localtime())
url = global_conf.url


# project_dir = os.path.abspath(os.path.dirname(__file__).split('pytest')[0]) + '/pytest'

def assertion(response, exp_code=200):
    '''封装断言'''
    assert response.status_code == exp_code
    dict_resp = json.loads(response.text)
    assert dict_resp.get('data', False)


def print_log(message):
    '''打印日志'''
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    # logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s : %(message)s')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
    # handler = logging.FileHandler('../log/'+format_time + '.log')
    # handler.setLevel(level=logging.INFO)
    # handler.setFormatter(formatter)
    console = logging.StreamHandler()
    console.setLevel(level=logging.INFO)
    console.setFormatter(formatter)
    # # logger.addHandler(handler)
    logger.addHandler(console)
    logger.info(message)


def get_token(resp_text):
    '''从response_text中，获取token'''
    resp_dict = json.loads(resp_text)
    token = resp_dict['data']['token']
    return token


def post_request(post_dict):
    '''post请求'''
    comment = post_dict['comment']
    print(comment)
    path = post_dict['path']
    headers = post_dict['header']
    body = json.dumps(post_dict['body'])
    path = url + path
    print_log('path= ' + path + '\n' + 'headers= ' + str(headers) + '\n' + 'body= ' + str(body))
    response = requests.post(url=path, data=body, headers=headers)
    print_log("response= " + str(response.status_code) + response.text)
    return response


if __name__ == '__main__':
    print_log('haha')
