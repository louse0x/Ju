#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: 返回域名备案主体
"""
import json
from urllib.request import urlopen


def beian(domain):
    """
    :desc: ICP主体备案查询
    :param domain:
    :return:
    """
    res = urlopen("https://tapi.66sj.cn/api/url_icp?url={0}".format(domain)).read().decode('utf-8')
    res = json.loads(res)
    try:
        return res['data']
    except TypeError:
        return '暂无域名备案'
    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1
