#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: 返回DNS记录
"""
import json
import traceback
from urllib import request

from module.config import config


def dns(domain):
    """
    :desc: dns_1: https://dns-lookup.whoisxmlapi.com/api/documentation/making-requests
           dns_2: https://promptapi.com/marketplace/description/dns_lookup-api?txn=free&live_demo=show
           dns_3: http://dns.bufferover.run/dns?q={domain}
    :param domain:
    :return:
    """
    try:
        data = dict()
        # dns_1
        res = request.urlopen(
            'https://www.whoisxmlapi.com/whoisserver/DNSService?apiKey={0}&domainName={1}&type=_all&outputFormat=json'.format(
                config(node='whois',
                       key='whoisxmlapi'), domain), timeout=30).read().decode('utf-8')
        data['dns_1'] = json.loads(res)
        # dns_2
        # TODO:: RANDOM HEADERS
        req = request.Request('https://api.promptapi.com/dns_lookup/api/any/{0}'.format(domain),
                              headers={"apikey": config(node='market', key='promptapi'),
                                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.44'},
                              method='GET')
        res_ = request.urlopen(req).read().decode('utf-8')
        data['dns_2'] = json.loads(res_)
        # dns_3
        res__ = request.urlopen(
            'http://dns.bufferover.run/dns?q={0}'.format(domain), timeout=30).read().decode('utf-8')
        data['dns_3'] = json.loads(res__)
        return data
    except Exception as e:
        traceback.print_exc()
        print(e)
        return -1
    return
