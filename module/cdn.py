#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: cdn
"""
import json
from urllib import request
from urllib.parse import urlencode


def cdn(domain):
    """
    :desc: cdn_1: http://tools.bugscaner.com/api/whichcdn/
           cdn_2: https://myssl.com/api/v1/tools/cdn_check?domain={domain}
    :param domain:
    :return:
    """
    try:
        data = dict()
        # cdn_1

        params = bytes(urlencode({'url': domain}), 'utf-8')
        req = request.Request('http://tools.bugscaner.com/api/whichcdn/', params)
        res = request.urlopen(req).read().decode('utf-8')
        data['cdn_1'] = json.loads(res)

        # cdn_2
        res_ = json.loads(request.urlopen('https://myssl.com/api/v1/tools/cdn_check?domain={0}'.format(domain),
                                          timeout=30).read().decode(
            'utf-8'))
        if res_['code'] == 0:
            data['cdn_2'] = res_['data']
        else:
            data['cdn_2'] = None

        return data
    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1
