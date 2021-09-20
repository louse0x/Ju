#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: dispatcher
"""
import json
import threading
from datetime import datetime
from pathlib import Path

from waf import waf

BASE_DIR = Path.cwd().parent
RESULT_DIR_PATH = BASE_DIR / 'result'
LOG_DIR_PATH = BASE_DIR / 'log'
# log & result判断填充
if not RESULT_DIR_PATH.exists():
    RESULT_DIR_PATH.mkdir()
if not LOG_DIR_PATH.exists():
    LOG_DIR_PATH.mkdir()

# 格式化时间字符串
TIME_FORMAT = datetime.strftime(datetime.today(), "%Y%m%d_%H%M%S")


class MyThread(threading.Thread):

    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None


def task(domain):
    keyword_list = ['geoip', 'beian', 'ga', 'whois', 'whatweb', 'dns', 'subdomain', 'cdn', 'waf']
    data = dict()
    li = []
    # 数据填充
    for keyword in keyword_list:
        t = MyThread(eval(keyword), args=(domain,))
        li.append(t)
        t.start()
    for i, t in enumerate(li):
        t.join()
        data[keyword_list[i]] = t.get_result()

    return data


print(json.dumps(task('tjhzyl.com'), ensure_ascii=False))
