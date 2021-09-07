#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":description :调度文件 调用所有其他Py文件皆以返回值的形式 在此文件进行处理
    :return
"""

from pathlib import Path
from datetime import datetime
from icp import *

BASE_DIR = Path.cwd().parent
RESULT_DIR_PATH = BASE_DIR / 'result'
LOG_DIR_PATH = BASE_DIR / 'log'
# log&result判断填充
if not RESULT_DIR_PATH.exists():
    RESULT_DIR_PATH.mkdir()
if not LOG_DIR_PATH.exists():
    LOG_DIR_PATH.mkdir()

# 格式化时间字符串
TIME_FORMAT = datetime.strftime(datetime.today(), "%Y%m%d_%H%M%S")

data_dict = dict()


def domain_task(domain):
    # icp数据填充 -> icp.py
    icp(domain)
    ga(domain)
    # TODO
    possess(domain)
    data_dict['icp'] = icp_dict
    return


# TODO
def ip_task(ip):
    pass
    return


domain_task('tjhzyl.com')
print(data_dict)
