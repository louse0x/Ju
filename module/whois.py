#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

from config import config
from urllib.request import urlopen


def whois(domain):
    """
    :desc: 返回域名whois信息
    :param domain:
    :return:
    """
    try:
        res = urlopen(
            'https://www.whoisxmlapi.com/whoisserver/WhoisService?outputFormat=json&apiKey={0}&domainName={1}'.format(
                config(node='whois',
                       key='whoisxmlapi'), domain),
            timeout=15).read().decode(
            "utf-8")
        return res
    except Exception as e:
        # TODO LOG ERROR
        print(e)
        return -1
