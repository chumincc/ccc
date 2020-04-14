# -*- coding:utf-8 -*-
import pytest
from src.utils import common
from appium import webdriver
from src.utils.common import create_dir,current_time
import os
import inspect

driver = None


@pytest.fixture(scope="session",autouse=True)
def get_driver():
    global driver
    attr = common.startup_conf()
    try:
        driver = webdriver.Remote("http://localhost:%s/wd/hub" % 4723, attr)
    except:
        raise Exception('启动driver失败！')
    return driver


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            #分割字符，取测试名，分割符为：[，::
            file_name = report.nodeid.rsplit('::',1)[1].split("[",1)[0] + current_time()[1] + ".png"
            screen_img = _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="%s" style="width:170px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % (screen_img,file_name)
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    if driver:
        screenshot_path = create_dir('screenshot')
        screenshot_pic = os.path.join(screenshot_path , name)
        driver.get_screenshot_as_file(screenshot_pic)
        return driver.get_screenshot_as_base64()
    else:
        print('driver is none!')
