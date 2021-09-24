#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: nmap
"""
import nmap3

from module.config import config


def jnmap(ip):
    """
    :desc: https://pypi.org/project/python3-nmap/
    :param ip:
    :return:
    """
    try:
        data = dict()
        nmap = nmap3.Nmap(path=config(node='nmap', key='path'))
        if nmap.nmap_version():
            # Linux may be need root
            data['ports'] = nmap.scan_top_ports(ip)
            # data['dns'] = nmap.nmap_dns_brute_script(ip)
            data['os'] = nmap.nmap_os_detection(ip)
            # data['sub'] = nmap.nmap_subnet_scan(ip)
            return data
        else:
            return 'nmap error'
    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1
