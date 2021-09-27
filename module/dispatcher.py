#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: dispatcher
"""
import json
import threading
from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

modules = ['geoip', 'beian', 'ga', 'whois', 'whatweb', 'dns', 'subdomain', 'cdn', 'waf', 'jssl',
           'whoisreverse', 'jnmap']

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
    """
    :desc: 主任务
    :param domain:
    :return:
    """
    data = dict()
    li = []
    # 数据填充
    for keyword in modules:
        t = MyThread(eval(keyword), args=(domain,))
        li.append(t)
        t.start()
    for i, t in enumerate(li):
        t.join()
        data[modules[i]] = t.get_result()

    return data


def raw(domain, data):
    # save raw file
    try:
        data = json.dumps(data)
        filename = domain + '_' + TIME_FORMAT
        # 写json文件
        # with open(str(RESULT_DIR_PATH) + '/' + filename + '.json', 'w+') as f:
        #     f.write(data)

        # 写html文件
        env = Environment(loader=FileSystemLoader('../'))
        template = env.get_template('template.html')

        with open(str(RESULT_DIR_PATH) + '/' + filename + '.html', 'w+', encoding='utf-8') as f_out:
            html = template.render(task=domain, datetime=TIME_FORMAT, geoip='')
            f_out.write(html)

    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1


# 调度
# raw_data = task('tjhzyl.com')
# print(raw_data)
env = Environment(loader=FileSystemLoader('../'))
template = env.get_template('template.html')
geoip_dict = {'continent': '亚洲', 'continentCode': 'AS', 'country': '中国', 'countryCode': 'CN', 'region': 'BJ',
              'regionName': '北京市', 'city': '北京', 'district': '', 'zip': '', 'lat': 39.9285, 'lon': 116.385,
              'timezone': 'Asia/Shanghai', 'offset': 28800, 'isp': 'ALICLOUD', 'org': 'Aliyun Computing Co.',
              'as': 'AS37963 Hangzhou Alibaba Advertising Co.,Ltd.', 'asname': 'CNNIC-ALIBABA-CN-NET-AP',
              'ip': '8.140.99.84', 'route': '8.140.99.0/24', 'asdomain': 'http://alibabagroup.com/', 'asn': 37963}
beian_dict = {'date': '2021-05-31', 'domain': 'www.tjhzyl.com', 'icp': '津ICP备2021004158号',
              'organizers': '天津华中医学美容专科有限公司', 'site': '企业', 'type': '天津华中医学美容专科有限公司'}
ga_dict = {'website_name': '网易', 'domain': '163.com', 'subject': '企业单位', 'category': '交互式',
           'organizer': '广州网易计算机系统有限公司', 'ga_id': '44010602006299', 'ga_location': '广东省广州市天河区网安大队',
           'ga_date': '2019-03-26'}
whois_dict = {}
waf_string = "Baidu Yunjiasu"
cdn_dict= {'info': 'CDN服务商指纹库有待增加,暂时未识别出这个网站所采用的CDN加速服务!', 'secess': False, 'ping': [{'ip': '220.181.107.181', 'location': '北京'}, {'ip': '112.34.111.167', 'location': '北京'}, {'ip': '153.37.235.50', 'location': '江苏苏州'}, {'ip': '182.61.200.129', 'location': '北京'}]}
with open(str(RESULT_DIR_PATH) + '/' + 'aaa.com' + '.html', 'w+', encoding='utf-8') as f_out:
    html = template.render(task='aaa.com', datetime=datetime.strftime(datetime.today(), "%Y-%m-%d %H:%M:%S"),
                           geoip_dict=geoip_dict, beian_dict=beian_dict, ga_dict=ga_dict, whois_dict=whois_dict,
                           waf_string=waf_string,cdn_dict=cdn_dict,)
    f_out.write(html)

# raw_res = raw('tjhzyl.com', test_data)
# if raw_res != -1:
#     # 正常
#     print(raw_res)
#     pass
# else:
#     # 异常
#     pass
