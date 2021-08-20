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


from base.action import ElementActions
from lib.pages.set import ProductPages as p
from base.verify import NotFoundTextError
from base.utils import log

#测试用例demo，pytest框架自动加载执行



class Test_demo():


    def test_home(self, action: ElementActions):

        # up.登录页.login(action,'13550234762','tmhrush2233')


        action.click(p.特卖首页.搜索输入框)

        #因为调用action的大部分公用方法是返回self，所以可以一条语句执行多次不同方法
        action.text(p.分类列表搜索页.搜索输入框,"口红")\
            .click(p.分类列表搜索页.搜索按钮)

        action.click(p.搜索后列表页.第一个商品项)

        #循环下拉，检查是否有对应关键字，找到后终止
        for count in range(20):
            if action.swip_down().is_text_displayed("商品参数"):
                break
        #没有对应关键字抛出错误
        if action.is_text_displayed("口红") ==False:
            raise NotFoundTextError

        action.sleep(1)
