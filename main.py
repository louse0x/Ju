#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:author Louse0x



"""

import argparse
from rich.console import Console

console = Console()


def main():
    # 创建参数解析
    parser = argparse.ArgumentParser(description="脚本描述：暂无", prog="Ju")
    parser.add_argument('-v', '--version', action='version', version="%(prog)s 1.0.0dev")
    parser.add_argument('-t', '--target', help='Please give me a target', required=True)

    # 接受参数并解析
    args = parser.parse_args()
    if args.target:
        console.print("The target is: %s" % args.target)
    else:
        console.print("Not giving a specific goal!")
        return


if __name__ == '__main__':
    console.print('Hello', 'Ju!', style="bold blue")
    main()
else:
    console.print("987")

