#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: ssl subdomain
"""
import re
from urllib import request
from tldextract import tldextract

from module.header import header
from bs4 import BeautifulSoup


def jssl(domain):
    # get root domain
    ext = tldextract.extract(domain)
    domain = ext.domain + '.' + ext.suffix

    try:
        data = dict()
        # jssl_1
        req = request.Request('https://crt.sh/?q={0}'.format(domain), headers={'User-Agent': header()})
        res = request.urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(res, 'lxml')
        td_list = [x for x in soup.find_all(text=re.compile(domain)) if ' ' not in x]
        data['jssl_1'] = set(td_list)
        return data

    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1
        pass


print(jssl('www.tjhzyl.com'))
