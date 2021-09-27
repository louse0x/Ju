#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: cdn
"""
import json
import traceback
import urllib.error
from urllib import request
from urllib.parse import urlencode

from module.header import header


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
        req = request.Request('http://tools.bugscaner.com/api/whichcdn/', params, headers={'User-Agent': header()})
        res = request.urlopen(req).read().decode('utf-8')
        data['cdn_1'] = json.loads(res)

        # cdn_2
        req_ = request.Request('https://myssl.com/api/v1/tools/cdn_check?domain={0}'.format(domain),
                               headers={'User-Agent': header()})
        res_ = json.loads(request.urlopen(req_).read().decode('utf-8'))
        if res_['code'] == 0:
            data['cdn_2'] = res_['data']
        else:
            data['cdn_2'] = None

        # 过滤重组
        return_data = {
            'info': data['cdn_1']['info'],
            'secess': data['cdn_1']['secess'],
            'ping': data['cdn_2']
        }
        return return_data
    except urllib.error.HTTPError:
        return 'Cdn HTTPError'
    except Exception as e:
        traceback.print_exc()
        return {}
