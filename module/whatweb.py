#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: 返回中间件识别
"""
from config import config

from urllib import request


def whatweb(target):
    """
    :desc: https://www.wappalyzer.com/docs/api/v2/lookup/
    :param target:
    :return:
    """
    try:
        # TODO:: RANDOM HEADERS
        req = request.Request('https://api.wappalyzer.com/lookup/v2/?urls={0}'.format(target),
                              headers={'x-api-key': config(node='whatweb', key='wappalyzer'),
                                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.44'})
        print('https://api.wappalyzer.com/lookup/v2/?urls={0}'.format(target))
        res = request.urlopen(req).read().decode('utf-8')
        req.close()
        return res
    except Exception as e:
        print(e)
        return -1


print(whatweb('www.tjhzyl.com'))
