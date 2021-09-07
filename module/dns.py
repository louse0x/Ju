#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: 域名DNS记录
"""
import json
from urllib import request

dns_dict = dict()


def bufferover(domain):
    """
    :desc: https://dns.bufferover.run/dns?q=domain.com
    :param domain:
    :return:
    """
    # TODO:: RANDOM HEADERS
    req = request.Request("https://dns.bufferover.run/dns?q=" + domain, headers={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19'})
    res = request.urlopen(req).read().decode('utf-8')
    # str -> dict
    res = json.loads(res)
    try:
        global dns_dict
        dns_dict['DNS_A'] = res['FDNS_A']
        dns_dict['RDNS'] = res['RDNS']
    except Exception as e:
        print(e)
    return


bufferover('csdn.net')
print(dns_dict)
