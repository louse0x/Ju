#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: geoip
"""
import json
import traceback
import urllib.error
from urllib import request

from module.config import config
from module.header import header


def geoip(domain):
    """
    :desc: geo_1: https://hackerdomain.com/geoip-ip-location-lookup/
           geo_2: https://ip-geolocation.whoisxmlapi.com/api
    :param domain: ip or domain
    :return:
    """
    try:
        data = {}
        # geo1
        req = request.Request('http://ip-api.com/json/{0}?fields=58458111&lang=zh-CN'.format(domain),
                              headers={'User-Agent': header()})
        res = json.loads(request.urlopen(req).read().decode('utf-8').split('\n')[0])
        data['geo_1'] = res if res['status'] == 'success' else None

        # geo2

        if data['geo_1'] is not None:
            req_ = request.Request(
                'https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey={0}&ipAddress={1}'.format(config(node='whois',
                                                                                                       key='whoisxmlapi'),
                                                                                                data['geo_1'][
                                                                                                    'query']),
                headers={'User-Agent': header()})
            res_ = request.urlopen(req_).read().decode('utf-8')
            data['geo_2'] = json.loads(res_)
        else:
            data['geo_2'] = None

        # 过滤重组
        return_data = {}
        if data['geo_1']:
            return_data['continent'] = data['geo_1']['continent']
            return_data['continentCode'] = data['geo_1']['continentCode']
            return_data['country'] = data['geo_1']['country']
            return_data['countryCode'] = data['geo_1']['countryCode']
            return_data['region'] = data['geo_1']['region']
            return_data['regionName'] = data['geo_1']['regionName']
            return_data['city'] = data['geo_1']['city']
            return_data['district'] = data['geo_1']['district']
            return_data['zip'] = data['geo_1']['zip']
            return_data['lat'] = data['geo_1']['lat']
            return_data['lon'] = data['geo_1']['lon']
            return_data['timezone'] = data['geo_1']['timezone']
            return_data['offset'] = data['geo_1']['offset']
            return_data['isp'] = data['geo_1']['isp']
            return_data['org'] = data['geo_1']['org']
            return_data['as'] = data['geo_1']['as']
            return_data['asname'] = data['geo_1']['asname']
            return_data['ip'] = data['geo_2']['ip']
            return_data['route'] = data['geo_2']['as']['route']
            return_data['asdomain'] = data['geo_2']['as']['domain']
            return_data['asn'] = data['geo_2']['as']['asn']
        else:
            return {}
        return return_data
    except urllib.error.HTTPError:
        return 'Geoip HTTPError'
    except Exception as e:
        traceback.print_exc()
        return {}
