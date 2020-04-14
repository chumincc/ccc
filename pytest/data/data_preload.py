#-*- coding:utf-8 -*-
'''
@author:liuchumin
@time:2020/4/132:07 下午
@desc:
'''

def post_data_preload(post_data,token,*kwgs):
    post_data['header']['X-HEAD-AUTH-TOKEN']=token
    print("------"+str(post_data))
    return post_data