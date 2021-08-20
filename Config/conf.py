'''
@Descripttion: 
@Author: zlj
@Date: 2020-06-03 15:47:09
'''
import os
import time
from selenium.webdriver.common.by import By
from datetime import datetime
# from utils.times import dt_strftime

# 获取当前目录的父目录的绝对路径
# 也就是整个工程的根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONF_PATH = os.path.join(ROOT_DIR, 'Config', 'location.ini')

DATA_Path = os.path.join(ROOT_DIR,'data','tcData.xlsx')


# 页面元素目录
element_path = os.path.join(ROOT_DIR, 'page_element')

# 报告文件
report_dir = os.path.join(ROOT_DIR, 'report')


driver_dir = os.path.join(ROOT_DIR, 'libs','chromedriver.exe')

# 当前时间
current_time = datetime.now().strftime('%H_%M_%S')

# 年月日
today = time.strftime("%Y-%m-%d", time.localtime())

# 报告名称
HTML_NAME = 'testReport{}.html'.format(current_time )

# 测试报告和日志的目录
report_log_path = os.path.join(ROOT_DIR, "logs")

if os.path.exists(report_log_path):
    pass
else:
    os.mkdir(report_log_path, mode=0o777)

logging_file = os.path.join(report_log_path, "log{}.log".format(today))


import logging
from loguru import logger

# 关闭sys.stderr，即关闭console输出
logger.remove(handler_id=None)

class PropogateHandler(logging.Handler):
    def emit(self, record):
        logging.getLogger(record.name).handle(record)

logger.add(PropogateHandler(), format="{time:YYYY-MM-DD HH:mm:ss}|{level}|{message}")



class Loggings:
    __instance = None
    logger.add(logging_file,
               format="{time:YYYY-MM-DD HH:mm:ss}|{level}|{message}",
               encoding="utf-8",
               rotation="00:00",
               retention="3 days",
               compression="zip",
               )

    # 类单例模式运行logger

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Loggings, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def trace(self, msg):
        return logger.trace(msg)

    def debug(self, msg):
        return logger.debug(msg)

    def info(self, msg):
        return logger.info(msg)

    def success(self, msg):
        return logger.success(msg)

    def warning(self, msg):
        return logger.warning(msg)

    def error(self, msg):
        return logger.error(msg)

    def critical(self, msg):
        return logger.critical(msg)
# loguru日志配置