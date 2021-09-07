#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: 返回域名备案主体及该备案下所有备案号、域名
"""
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

icp_dict = {
    "icp": dict(),
    "ga": dict()
}


def icp(domain):
    """
    :desc: ICP主体备案查询
    :param domain:
    :return:
    """
    res = urlopen("https://tapi.66sj.cn/api/url_icp?url=" + domain).read().decode('utf-8')
    # str -> dict
    res = json.loads(res)
    global icp_dict
    try:
        icp_dict['icp']['id'] = res['data']['icp']
        icp_dict['icp']['organizers'] = res['data']['organizers']
        icp_dict['icp']['type'] = res['data']['site']
        icp_dict['icp']['site'] = res['data']['type']
    except TypeError:
        icp_dict['icp']['id'] = '暂无域名备案'

    return


def ga(domain):
    """
    :desc: 公安网备查询
    :param domain:
    :return:
    """
    res = urlopen("https://api88.net/api/wa/?name=" + domain).read().decode('utf-8')
    soup = BeautifulSoup(res, 'html.parser')
    global icp_dict
    try:
        tbody = soup.table.find_all('td')
        ga_list = [child.get_text() for child in tbody]
        # 填充公安网备
        icp_dict['ga']['id'] = ga_list[-5][:-6]
        icp_dict['ga']['date'] = ga_list[-1]
    except AttributeError:
        # 无公安网备
        icp_dict['ga']['id'] = '暂无公安网备'

    return


def possess(organizers):
    """
    :desc: 同主体备案号查询
    :param organizers:
    :return:
    """
    # TODO
    return


if __name__ == '__main__':
    del icp_dict
    print('Illegal call')
