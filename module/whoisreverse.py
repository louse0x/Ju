#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: whois reverse
"""
import json
from urllib import request
from urllib.parse import quote
from tldextract import tldextract

from module.header import header


def whoisreverse(domain):
    """
    :desc: http://whois.4.cn/api/whoisreverse-domain?domain={domain}
    :param domain:
    :return:
    """
    # get root domain
    ext = tldextract.extract(domain)
    domain = ext.domain + '.' + ext.suffix

    try:
        data = dict()
        headers = {'User-Agent': header()}

        # whois反查
        req = request.Request('http://whois.4.cn/api/whoisreverse-domain?domain={0}'.format(domain), headers=headers)
        res = json.loads(request.urlopen(req).read().decode('utf-8'))

        if res['retcode'] == 0:
            # 执行正常流程

            # 注册人单位反查
            req_ = request.Request(
                'http://whois.4.cn/api/whoisreverse?keyword={0}&type=org'.format(quote(res['data']['org'])),
                headers=headers)
            res_ = json.loads(request.urlopen(req_).read().decode('utf-8'))
            if res_['retcode'] == 0:
                data['reverse_org'] = res_['data']
            else:
                data['reverse_org'] = "reverse_org none"

            # 注册人邮箱反查
            req__ = request.Request(
                'http://whois.4.cn/api/whoisreverse?keyword={0}&type=email'.format(quote(res['data']['email'])),
                headers=headers)
            res__ = json.loads(request.urlopen(req__).read().decode('utf-8'))
            if res__['retcode'] == 0:
                data['reverse_email'] = res__['data']
            else:
                data['reverse_email'] = "reverse_email none"

            # 注册人反查
            req___ = request.Request(
                'http://whois.4.cn/api/whoisreverse?keyword={0}&type=name'.format(quote(res['data']['name'])),
                headers=headers)
            res___ = json.loads(request.urlopen(req___).read().decode('utf-8'))
            if res___['retcode'] == 0:
                data['reverse_name'] = res___['data']
            else:
                data['reverse_name'] = "reverse_name none"
        else:
            # 查询失败
            return "whoisreverse error"
        # func return
        return data

    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1
