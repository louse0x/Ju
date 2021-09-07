#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from config import config
from urllib.request import urlopen
import os,time,json
from xml.etree.ElementTree import parse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

result_dir_path = os.path.join(BASE_DIR, "../result/")


def whois(domain):
    whois_dict = dict()

    res = urlopen('https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=' + config(node='whois',
                                                                                          key='whoisxmlapi') + '&domainName=' + domain).read().decode(
        "utf-8")
    result_file = '_'.join(['r',domain,time.strftime("%Y-%m-%d", time.localtime()),'.json'])
    # 存入result
    if not os.path.exists(result_dir_path):
        os.mkdir(result_dir_path)

    with open(file=result_dir_path+result_file,mode='w+',encoding='utf-8') as f:
        f.write(json.dumps(whois_dict))






    # 解析XML


    print(res)

    return


whois('qq.com')
