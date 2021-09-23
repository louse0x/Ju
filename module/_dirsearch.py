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
        # res, val = subprocess.getstatusoutput(
        #     "{0} {1}/dirsearch.py -u {2} --recursion-depth 3 --recursion-status 200-399 --exclude-texts='Not found','Error' --no-color --user-agent={3} --retries=1 --format=json --quiet-mode -e php,htm,js,bak,zip,tgz,txt -t 20 --max-rate 100".format(
        #         executable, dirsearch.__path__[0], domain, header()))
        #
        # if res == 0:
        #     # 执行正常
        #     print(val)

        #         out_bytes = subprocess.check_output("{0} {1}/dirsearch.py -u {2} --recursion-depth 3 --recursion-status 200-399 --exclude-texts='Not found','Error' --no-color --user-agent={3} --retries=1 --format=json --quiet-mode -e php,htm,js,bak,zip,tgz,txt -t 20 --max-rate 100".format(
        # executable, dirsearch.__path__[0], domain, header(),shell=True,timeout=60)
        proc = subprocess.Popen(
            "{0} {1}/dirsearch.py -u {2} --recursion-status 200-399 --exclude-status=400-599 --no-color --user-agent={3} --quiet-mode -e php,htm,js,bak,zip,tgz,txt -t 2 --format=json".format(
                executable, dirsearch.__path__[0], domain, header()), shell=True, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        # 防止使用wait()死锁
        (output, errout) = proc.communicate()
        if proc.returncode == 0:
            # 执行正常
            # 读文件
            return output
        else:
            return errout
    except subprocess.CalledProcessError as e:
        # TODO:: LOG ERROR
        return str([e.returncode, e.output.decode('utf-8')])
    except subprocess.TimeoutExpired as e:
        # TODO:: LOG ERROR
        return "dirsearch timeout"


print(_dirsearch('testphp.vulnweb.com'))
