#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: ssl subdomain
"""
from urllib import request
from tldextract import tldextract

from module.header import header


def jssl(domain):
    # get root domain
    ext = tldextract.extract(domain)
    domain = ext.domain + '.' + ext.suffix

    try:
        req = request.Request('https://crt.sh/?q={0}'.format(domain), headers={'User-Agent': header()})
        res = request.urlopen(req).read().decode('utf-8')
        print(res)


    except Exception as e:
        pass


print(j_ssl('www.tjhzyl.com'))
