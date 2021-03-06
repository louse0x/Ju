#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: whatweb
"""
import json
from urllib import request
from urllib.parse import urlencode

from module.config import config
from module.header import header


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
                     'User-Agent': header()})
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
