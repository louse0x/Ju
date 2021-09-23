#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: dispatcher
"""
import json
import threading
from datetime import datetime
from pathlib import Path
from collections import defaultdict

from geoip import geoip
from beian import beian
from ga import ga
from whois import whois
from whatweb import whatweb
from dns import dns
from subdomain import subdomain
from cdn import cdn
from waf import waf
from whoisreverse import whoisreverse

BASE_DIR = Path.cwd().parent
RESULT_DIR_PATH, LOG_DIR_PATH, TEMP_DIR_PATH, = BASE_DIR / 'result', BASE_DIR / 'log', BASE_DIR / 'temp'

# sub dir
if not RESULT_DIR_PATH.exists():
    RESULT_DIR_PATH.mkdir()
if not LOG_DIR_PATH.exists():
    LOG_DIR_PATH.mkdir()
if not TEMP_DIR_PATH.exists():
    TEMP_DIR_PATH.mkdir()

# 格式化时间字符串
TIME_FORMAT = datetime.strftime(datetime.today(), "%Y-%m-%d_%H-%M-%S")


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
    data = defaultdict(keyword_list)
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


def raw(domain, data):
    # raw file
    try:
        with open(str(RESULT_DIR_PATH) + '/' + domain + '_' + TIME_FORMAT + '.json', 'w+') as f:
            f.write(json.dumps(data))
        return 0
    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1


raw('aaa.test.com', {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'})
# print(json.dumps(task('tjhzyl.com'), ensure_ascii=False))
