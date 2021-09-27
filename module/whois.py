#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: whois
"""
import json
import traceback
import urllib.error
from urllib import request

from module.config import config
from module.header import header


def whois(domain):
    """
    :desc: whois_1: https://whois.whoisxmlapi.com/
           whois_2: https://www.whoxy.com/whois-lookup/demo.php
    :param domain:
    :return:
    """
    try:
        data = dict()
        # whois_1
        req = request.Request(
            'https://www.whoisxmlapi.com/whoisserver/WhoisService?outputFormat=json&apiKey={0}&domainName={1}'.format(
                config(node='whois',
                       key='whoisxmlapi'), domain), headers={'User-Agent': header()})
        data['whois_1'] = json.loads(request.urlopen(req).read().decode("utf-8"))

        # whois_2
        req_ = request.Request('https://ipwhois.app/json/{0}'.format(domain),
                               headers={'User-Agent': header()})
        data['whois_2'] = json.loads(request.urlopen(req_).read().decode("utf-8"))

        # 过滤重组
        return_data = {
            'createdDate': data['whois_1']['WhoisRecord']['createdDate'],
            'updatedDate': data['whois_1']['WhoisRecord']['updatedDate'],

            'expiresDate': data['whois_1']['WhoisRecord']['expiresDate'],

            'name': data['whois_1']['WhoisRecord']['registrant']['name'],

            'organization': data['whois_1']['WhoisRecord']['registrant']['organization'],

            'street1': data['whois_1']['WhoisRecord']['registrant']['street1'],

            'city': data['whois_1']['WhoisRecord']['registrant']['city'],

            'state': data['whois_1']['WhoisRecord']['registrant']['state'],

            'postalCode': data['whois_1']['WhoisRecord']['registrant']['postalCode'],

            'country': data['whois_1']['WhoisRecord']['registrant']['country'],

            'countryCode': data['whois_1']['WhoisRecord']['registrant']['countryCode'],

            'telephone': data['whois_1']['WhoisRecord']['registrant']['telephone'],

            'telephoneExt': data['whois_1']['WhoisRecord']['registrant']['telephoneExt'],

            'fax': data['whois_1']['WhoisRecord']['registrant']['fax'],

            'faxExt': data['whois_1']['WhoisRecord']['registrant']['faxExt'],

            'createdDate': data['whois_1']['WhoisRecord'],

            'createdDate': data['whois_1']['WhoisRecord'],

            'createdDate': data['whois_1']['WhoisRecord'],

            'createdDate': data['whois_1']['WhoisRecord']

        }

        return return_data
    except urllib.error.HTTPError:
        return 'Whois HTTPError'
    except Exception as e:
        traceback.print_exc()
        return {}
# TODO