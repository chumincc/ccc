# -*- coding:utf-8 -*-
import pytest
from src.utils import common
from appium import webdriver


@pytest.fixture(scope="session")
def get_driver():
    attr = common.startup_conf()
    driver = webdriver.Remote("http://localhost:%s/wd/hub" % 4723, attr)
    return driver

