#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: 返回nmap扫描
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
            data['version_detection'] = nmap.nmap_version_detection(ip)
        else:
            return data
    except Exception as e:
        print(e)
        return -1


print(_nmap('8.140.99.84'))
