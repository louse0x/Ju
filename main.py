#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:author Louse0x



"""

import argparse, os
import sys
from urllib.request import urlopen

from rich.console import Console
import re
from module.whois import whois

console = Console()


def main():



    # 创建参数解析
    parser = argparse.ArgumentParser(description="脚本描述：暂无", prog="Ju")
    parser.add_argument('-v', '--version', action='version', version="%(prog)s 1.0.0dev")
    parser.add_argument('-t', '--target', help='Please give me a target', required=True)
    # -c/--clean 清洁参数 清理log&result下所有数据
    parser.add_argument('-c', '--clean', help='This operation will delete all the data in the log and result '
                                              'folders!Careful!!!')

    # 接受参数并解析
    args = parser.parse_args()

    # 清理
    if args.clean:
        # log文件夹
        with os.scandir('log') as entries:
            for entry in entries:
                os.remove(entry)
        # result文件夹
        with os.scandir('result') as entries:
            for entry in entries:
                os.remove(entry)
        return

    # 联通性测试
    http_code = urlopen('https://www.google.com.hk/').getcode()
    if http_code == '200' or http_code == '201':
        # TODO:: DO DISPATCHER
        pass
    else:
        # TODO:: PASS
        pass


if __name__ == '__main__':
    if sys.hexversion < '':
        # TODO
        sys.stderr.write('\r\n')

    console.print('Hello', 'Ju!', style="bold blue")
    main()
else:
    console.print("987")
