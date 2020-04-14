#-*- coding: UTF-8 -*-
import pytest
if __name__ == '__main__':
    #失败重试reruns
    pytest.main(['-q',
                 'testcase/test_post.py',
                 '--reruns=0',
                 '--html=./report/report.html',
                 '--self-contained-html'])