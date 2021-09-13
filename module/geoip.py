#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: 返回服务器IP地址Geo
"""
from urllib.request import urlopen


def geoip(target):
    """
    :desc: https://hackertarget.com/geoip-ip-location-lookup/
    :param target: ip or domain
    :return:
    """
    try:
        req = urlopen('http://ip-api.com/json/{0}?fields=58458111&lang=zh-CN'.format(target), timeout=5)
        res = req.read().decode('utf-8').split('\n')
        req.close()
        return res[0]
    except Exception as e:
        # TODO LOG ERROR
        print(e)
        return -1
