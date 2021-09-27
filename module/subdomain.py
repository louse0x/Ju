#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: subdomain
"""
import json
import traceback
import urllib
from urllib import request

from module.header import header


def subdomain(domain):
    """
    :desc: sub_1: https://myssl.com/api/v1/discover_sub_domain?domain={domain}
    :param domain:
    :return:
    """
    try:
        # sub_1
        data = {}
        req = request.Request('https://myssl.com/api/v1/discover_sub_domain?domain={0}'.format(domain),
                              headers={'User-Agent': header()})
        res = json.loads(
            request.urlopen(req).read().decode('utf-8'))
        if res['code'] == 0:
            # 正常返回
            data['sub_1'] = res['data']
        return data
    except urllib.error.HTTPError:
        return 'Subdomain HTTPError'
    except Exception as e:
        traceback.print_exc()
        return {}



print(subdomain('tjhzyl.com'))