#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: nmap
"""
import traceback

import nmap3

from module.config import config


def jnmap(domain):
    """
    :desc: https://pypi.org/project/python3-nmap/
    :param domain:
    :return:
    """
    try:
        data = {}
        nmap = nmap3.Nmap(path=config(node='nmap', key='path'))
        if nmap.nmap_version():
            # Linux may be need root
            data['ports'] = nmap.scan_top_ports(domain)
            # data['dns'] = nmap.nmap_dns_brute_scrdomaint(domain)
            data['os'] = nmap.nmap_os_detection(domain)
            # data['sub'] = nmap.nmap_subnet_scan(domain)
            return data
        else:
            return 'nmap error'
    except Exception as e:
        traceback.print_exc()
        return {}
print(jnmap('www.tjmylike.com'))