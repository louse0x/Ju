#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: Web path scanner
"""

import subprocess
from sys import executable

import dirsearch

from header import header


def _dirsearch(domain):
    """
    :desc: https://github.com/maurosoria/dirsearch
    :param domain
    :return:
    """
    try:
        proc = subprocess.Popen(
            "{0} {1}/dirsearch.py -u {2} --recursion-status 200-399 --no-color --user-agent={3} --quiet-mode -e php,htm,js,bak,zip,tgz,txt -t 2 --format=json".format(
                executable, dirsearch.__path__[0], domain, header()), shell=True, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        # proc = subprocess.Popen(
        #     "ping www.baidu.com".format(
        #         executable, dirsearch.__path__[0], domain, header()), shell=True, stdout=subprocess.PIPE,
        #     stderr=subprocess.PIPE)
        # 防止使用wait()死锁
        # output, errout = proc.communicate()
        # print(output,errout)
        proc.wait()
        if proc.returncode == 0:
            # 执行正常
            # 读文件
            return proc
        else:
            return proc
    except subprocess.CalledProcessError as e:
        # TODO:: LOG ERROR
        return str([e.returncode, e.output.decode('utf-8')])
    except subprocess.TimeoutExpired as e:
        # TODO:: LOG ERROR
        return "dirsearch timeout"


print(_dirsearch('testphp.vulnweb.com'))
