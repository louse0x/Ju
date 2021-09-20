#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: TODO
"""
from urllib.request import urlopen

reverseip_dict = dict()


def reverseip(ip):
    """
    :desc: https://api.hackertarget.com/reverseiplookup/?q=2.2.2.2
    :param ip:
    :return:
    """

    try:
        res = urlopen('https://api.hackertarget.com/reverseiplookup/?q=' + ip).read().decode('utf-8')
        res = res.split('\n')
        # res = list(itertools.chain.from_iterable([item.split(':') for item in res]))
        res = [item.split(':') for item in res]
        global geoip_dict
        geoip_dict = {x[0]: x[1].strip() for x in res}

        print(res)

    except Exception as e:
        print(e)

    return
