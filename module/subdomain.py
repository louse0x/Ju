#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: subdomain
"""
import json
from urllib.request import urlopen


def subdomain(domain):
    """
    :desc: sub_1: https://myssl.com/api/v1/discover_sub_domain?domain={domain}
    :param domain:
    :return:
    """
    try:
        # sub_1
        data = dict()
        res = json.loads(
            urlopen('https://myssl.com/api/v1/discover_sub_domain?domain={0}'.format(domain)).read().decode('utf-8'))
        if res['code'] == 0:
            # 正常返回
            data['sub_1'] = res['data']
        return data
    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1
