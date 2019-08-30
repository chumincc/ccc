# -*- coding:utf-8 -*-
import pytest
from src.utils import common
from appium import webdriver
from src.utils.common import create_dir
import inspect

driver = None


@pytest.fixture(scope="session",autouse=True)
def get_driver():
    global driver
    attr = common.startup_conf()
    driver = webdriver.Remote("http://localhost:%s/wd/hub" % 4723, attr)
    return driver


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    print(item,'111111111111111')
    print(type(item))
    print(item.__class__.__name__)

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot('aa')
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(pic_name):
    screenshot_dir = create_dir('screenshot')
    pic = screenshot_dir + '\\'+ pic_name + '.png'
    driver.get_screenshot_as_file(pic)
    return driver.get_screenshot_as_base64()
