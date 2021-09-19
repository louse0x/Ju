#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: CDN识别
"""
import json, bs4
from urllib import request
from urllib.parse import urlencode


def cdn(domain):
    """
    :desc: cdn_1: http://tools.bugscaner.com/api/whichcdn/
    :param domian:
    :return:
    """
    try:
        # cdn_1
        data = dict()
        params = bytes(urlencode({'url': domain}), 'utf-8')
        req = request.Request('http://tools.bugscaner.com/api/whichcdn/', params)
        res = request.urlopen(req).read().decode('utf-8')
        data['cdn_1'] = json.loads(res)

        return data
    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1


print(cdn('tools.bugscaner.com'))
