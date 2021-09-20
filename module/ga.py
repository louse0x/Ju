#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: ga record
"""
from urllib.request import urlopen

from bs4 import BeautifulSoup


def ga(domain):
    """
    :desc: 公安网备查询
    :param domain:
    :return:
    """
    try:
        res = urlopen("https://api88.net/api/wa/?name=" + domain).read().decode('utf-8')
        soup = BeautifulSoup(res, 'html.parser')
        tbody = soup.table.find_all('td')
        ga_list = [child.get_text() for child in tbody][1::2]
        ga_list[-3] = ga_list[-3][:-6]
        key_list = ['website_name', 'domain', 'subject', 'category', 'organizer', 'ga_id', 'ga_location', 'ga_date']
        # 填充数据返回
        return dict(zip(key_list, ga_list))
    except AttributeError:
        # 无公安网备
        return '暂无公安网备'
    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1
