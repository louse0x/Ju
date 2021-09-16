#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import json
from urllib.request import urlopen
from config import config


def whois(domain):
    """
    :desc: whois_1: https://whois.whoisxmlapi.com/
           whois_2: https://www.whoxy.com/whois-lookup/demo.php
    :param domain:
    :return:
    """
    data = dict()
    try:
        # whois_1
        res = urlopen(
            'https://www.whoisxmlapi.com/whoisserver/WhoisService?outputFormat=json&apiKey={0}&domainName={1}'.format(
                config(node='whois',
                       key='whoisxmlapi'), domain),
            timeout=15).read().decode("utf-8")
        data['whois_1'] = json.loads(res)

        # whois_2
        # TODO:: RANDOM HEADERS
        res_ = urlopen('https://ipwhois.app/json/{0}'.format(domain)).read().decode('utf-8')
        data['whois_2'] = json.loads(res_)

        return data
    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1
