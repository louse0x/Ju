#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: nmap
#TODO
"""
import nmap3

from module.config import config


def _nmap(ip):
    """
    :desc: https://pypi.org/project/python3-nmap/
    :param ip:
    :return:
    """
    try:
        data = dict()
        nmap = nmap3.Nmap(path=config(node='nmap', key='path'))
        print(config(node='nmap', key='path'))
        if nmap.nmap_version():
            # Linux may be need root
            data['ports'] = nmap.scan_top_ports(ip)
            data['dns'] = nmap.nmap_dns_brute_script(ip)
            data['os'] = nmap.nmap_os_detection(ip)
            data['sub'] = nmap.nmap_subnet_scan(ip)
        else:
            return data
    except Exception as e:
        print(e)
        return -1


print(_nmap('8.140.99.84'))
