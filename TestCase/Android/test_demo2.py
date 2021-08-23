# -*-coding:utf-8 -*-
# File : test_demo2.py
# @Time : 2021/8/20 18:42
# @Author : Sf
# version : python 3.7.8

import pytest
import time
from utils.parseExcelFile import ParseExcel
from Config.conf import *
import allure


@allure.feature('search功能')
# @pytest.mark.loginTest
class TestSearch(object):
    """登录"""
    data = ParseExcel()
    sheet = data.get_sheet_by_name('login')

    # 数据源使用Excel
    @allure.story('login_faild')
    # @pytest.mark.skip()
    @pytest.mark.parametrize('username, password, expect', data.get_all_values_of_sheet(sheet))
    def test_fail(self, open_url, username, password, expect):
        logger.info("搜索测试")
        login_page = open_url
        login_page.login(username, password)
        # actual = login_page.get_error_text()
        # print("expect:{},actual:{}".format(expect,actual))
        # assert actual == expect, "登录失败, 断言失败"

