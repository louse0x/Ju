#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: ga record
"""
import traceback
import urllib.error
from urllib import request

from bs4 import BeautifulSoup

from module.header import header


def ga(domain):
    """
    :desc: 公安网备查询
    :param domain:
    :return:
    """
    try:
        req = request.Request("https://api88.net/api/wa/?name=" + domain, headers={'User-Agent': header()})
        res = request.urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(res, 'html.parser')
        tbody = soup.table.find_all('td')
        ga_list = [child.get_text() for child in tbody][1::2]
        ga_list[-3] = ga_list[-3][:-6]
        key_list = ['website_name', 'domain', 'subject', 'category', 'organizer', 'ga_id', 'ga_location', 'ga_date']
        # 填充数据返回
        return dict(zip(key_list, ga_list))
    except AttributeError:
        # 无公安网备
        return {}
    except urllib.error.HTTPError:
        return 'Ga HTTPError'
    except Exception as e:
        traceback.print_exc()
        return {}
