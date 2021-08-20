# -*-coding:utf-8 -*-
# File : Run.py
# @Time : 2021/8/20 17:55
# @Author : Sf
# version : python 3.7.8

import sys
import os
import pytest
# import utils.send_mail

# from config.project_config import *
# import zmail
#
#
# REPORT_FILE = "./Report/report_html/Report.html"
# def send_report():
#     """发送报告"""
#     with open(REPORT_FILE, encoding='utf-8') as f:
#         content_html = f.read()
#     try:
#         mail = {
#             'from': '419406847@qq.com',
#             'subject': '最新的测试报告邮件',
#             'content_html': content_html,
#             'attachments': [REPORT_FILE, ]
#         }
#         server = zmail.server(*email_info.values())
#         server.send_mail(*address, mail)
#         print("测试邮件发送成功！")
#     except Exception as e:
#         print("Error: 无法发送邮件，{}！", format(e))



if __name__ == "__main__":
    # pytest.main()
    pytest.main(["./TestCase/test_loginCase.py"])
    # pytest.main(["./test_cases/test_CustCircle.py"])
    # pytest.main(["./test_cases/test_Breakbulk_Express_Contract.py"])
    # send_report()
    # os.system("allure serve ./Report/allure-result/")
    # os.system("allure generate ./Report/allure-result/ -o ./Report/allure-report/ --clean")