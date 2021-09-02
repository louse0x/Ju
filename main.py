#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:author Louse0x



"""

import argparse
from rich.console import Console
import re
from module.whois import whois

console = Console()


def main():
    # 创建参数解析
    parser = argparse.ArgumentParser(description="脚本描述：暂无", prog="Ju")
    parser.add_argument('-v', '--version', action='version', version="%(prog)s 1.0.0dev")
    parser.add_argument('-t', '--target', help='Please give me a target', required=True)

    # 接受参数并解析
    args = parser.parse_args()
    target = args.target
    if target:
        console.print("The target is: %s" % target)
    else:
        console.print("Not giving a specific goal!")
        return

    # 判断target是域名/IP
    if not re.findall(
            "^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|["
            "1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$",
            target):
        # whois收集
        whois(target)



if __name__ == '__main__':
    console.print('Hello', 'Ju!', style="bold blue")
    main()
else:
    console.print("987")
