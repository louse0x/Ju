#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: 返回中间件识别
"""
import json
from urllib import request
from urllib.parse import urlencode

from config import config


def whatweb(domain):
    """
    :desc: whatweb_1: https://www.wappalyzer.com/docs/api/v2/lookup/
           whatweb_2: http://whatweb.bugscaner.com/what.go
    :param domain:
    :return:
    """
    try:
        # whatweb_1
        data = dict()
        # TODO:: RANDOM HEADERS
        req = request.Request(
            'https://api.wappalyzer.com/lookup/v2/?urls=http://{0}'.format(domain, domain),
            headers={'x-api-key': config(node='whatweb', key='wappalyzer'),
                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.44'})
        res = request.urlopen(req).read().decode('utf-8')
        data['whatweb_1'] = json.loads(res)
        # whatweb_2
        params = bytes(urlencode({'url': domain}), 'utf-8')
        req_ = request.Request('http://whatweb.bugscaner.com/what.go', params)
        res_ = json.loads(request.urlopen(req_).read().decode('utf-8'))
        if res_['status'] == 99:
            data['whatweb_2'] = res_
        else:
            data['whatweb_2'] = None
        return data
    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1
