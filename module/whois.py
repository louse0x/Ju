#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from config import config
from urllib.request import urlopen
from xml.etree.ElementTree import parse



def whois(domain):
    whois_dict = dict()

    res = urlopen('https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=' + config(node='whois',
                                                                                          key='whoisxmlapi') + '&domainName=' + domain).read().decode(
        "utf-8")

    # 解析XML
    doc = iterparse(res, ('start', 'end'))


    print(res)

    return


whois('qq.com')
