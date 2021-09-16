#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: 返回服务器IP地址Geo
"""
import json
from urllib.request import urlopen
from module.config import config


def geoip(domain):
    data = dict()
    """
    :desc: geo_1: https://hackerdomain.com/geoip-ip-location-lookup/
           geo_2: https://ip-geolocation.whoisxmlapi.com/api
    :param domain: ip or domain
    :return:
    """
    try:
        # geo1
        req = urlopen('http://ip-api.com/json/{0}?fields=58458111&lang=zh-CN'.format(domain), timeout=5)
        res = json.loads(req.read().decode('utf-8').split('\n')[0])
        data['geo_1'] = res if res['status'] == 'success' else None

        # geo2
        res_ = urlopen(
            'https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey={0}&ipAddress={1}'.format(config(node='whois',
                                                                                                   key='whoisxmlapi'),
                                                                                            data['geo1'][
                                                                                                'query'])).read().decode(
            'utf-8')
        data['geo_2'] = json.loads(res_)
        return data
    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1
