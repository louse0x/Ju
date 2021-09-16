#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":description :调度文件 调用所有其他Py文件皆以返回值的形式 在此文件进行处理
    :return
"""
import json
from pathlib import Path
from datetime import datetime

from module.beian import beian
from module.ga import ga
from module.geoip import geoip
from module.whatweb import whatweb
from module.whois import whois

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


def task(domain):
    global data_dict
    # geo数据 -> geoip.py
    data_dict['geo'] = geoip(domain)
    # 备案数据 -> beian.py
    data_dict['beian'] = beian(domain)
    # 公安备案数据 -> ga.py
    data_dict['ga'] = ga(domain)
    # whois数据 -> whois.py
    data_dict['whois'] = whois(domain)
    # whatweb数据 -> whatweb.py
    data_dict['whatweb'] = whatweb(domain)

    return


task('tjhzyl.com')
print(json.dumps(data_dict, ensure_ascii=False))
