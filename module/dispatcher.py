#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: dispatcher
"""
import json
import threading
from datetime import datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from geoip import geoip
from beian import beian
from ga import ga
from whois import whois
from whatweb import whatweb
from dns import dns
from subdomain import subdomain
from cdn import cdn
from waf import waf
from whoisreverse import whoisreverse
from jssl import jssl
from jnmap import jnmap

modules = ['geoip', 'beian', 'ga', 'whois', 'whatweb', 'dns', 'subdomain', 'cdn', 'waf', 'jssl',
           'whoisreverse', 'jnmap']

BASE_DIR = Path.cwd().parent
RESULT_DIR_PATH, LOG_DIR_PATH, TEMP_DIR_PATH, = BASE_DIR / 'result', BASE_DIR / 'log', BASE_DIR / 'temp'

# sub dir
if not RESULT_DIR_PATH.exists():
    RESULT_DIR_PATH.mkdir()
if not LOG_DIR_PATH.exists():
    LOG_DIR_PATH.mkdir()
if not TEMP_DIR_PATH.exists():
    TEMP_DIR_PATH.mkdir()

# 格式化时间字符串
TIME_FORMAT = datetime.strftime(datetime.today(), "%Y-%m-%d_%H-%M-%S")


class MyThread(threading.Thread):

    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None


def task(domain):
    """
    :desc: 主任务
    :param domain:
    :return:
    """
    data = dict()
    li = []
    # 数据填充
    for keyword in modules:
        t = MyThread(eval(keyword), args=(domain,))
        li.append(t)
        t.start()
    for i, t in enumerate(li):
        t.join()
        data[modules[i]] = t.get_result()

    return data


def raw(domain, data):
    # save raw file
    try:
        data = json.dumps(data)
        filename = domain + '_' + TIME_FORMAT
        # 写json文件
        # with open(str(RESULT_DIR_PATH) + '/' + filename + '.json', 'w+') as f:
        #     f.write(data)

        # 写html文件
        env = Environment(loader=FileSystemLoader('../'))
        template = env.get_template('template.html')

        with open(str(RESULT_DIR_PATH) + '/' + filename + '.html', 'w+', encoding='utf-8') as f_out:
            html = template.render(task=domain, datetime=TIME_FORMAT,geoip=data['geoip'])
            f_out.write(html)

    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1


# 调度
# raw_data = task('tjhzyl.com')
# print(raw_data)
test_data = {'geoip': {'geo_1': {'status': 'success', 'continent': '亚洲', 'continentCode': 'AS', 'country': '中国', 'countryCode': 'CN', 'region': 'BJ', 'regionName': '北京市', 'city': '北京', 'district': '', 'zip': '', 'lat': 39.9285, 'lon': 116.385, 'timezone': 'Asia/Shanghai', 'offset': 28800, 'isp': 'ALICLOUD', 'org': 'Aliyun Computing Co.', 'as': 'AS37963 Hangzhou Alibaba Advertising Co.,Ltd.', 'asname': 'CNNIC-ALIBABA-CN-NET-AP', 'reverse': '', 'mobile': False, 'proxy': False, 'hosting': True, 'query': '8.140.99.84'}, 'geo_2': {'ip': '8.140.99.84', 'location': {'country': 'CN', 'region': 'Beijing Shi', 'city': 'Beijing', 'lat': 39.9075, 'lng': 116.39723, 'postalCode': '', 'timezone': '+08:00', 'geonameId': 1816670}, 'domains': ['tjhzyl.com'], 'as': {'asn': 37963, 'name': 'Alibaba (China)', 'route': '8.140.99.0/24', 'domain': 'http://alibabagroup.com/', 'type': 'Content'}, 'isp': 'Aliyun Computing Co.LTD', 'connectionType': ''}}, 'beian': {'date': '2021-05-31', 'domain': 'tjhzyl.com', 'icp': '津ICP备2021004158号', 'organizers': '天津华中医学美容专科有限公司', 'site': '企业', 'type': '天津华中医学美容专科有限公司'}, 'ga': '暂无公安网备', 'whois': {'whois_1': {'WhoisRecord': {'createdDate': '2021-05-11T03:23:02Z', 'updatedDate': '2021-05-11T03:41:17Z', 'expiresDate': '2026-05-11T03:23:02Z', 'registrant': {'name': 'Registry Registrant ID: Not Available From Registry', 'state': 'tian jin', 'country': 'CHINA', 'countryCode': 'CN', 'rawText': 'Registrant Country: CN\nRegistry Registrant ID: Not Available From Registry'}, 'domainName': 'tjhzyl.com', 'nameServers': {'rawText': 'VIP1.ALIDNS.COM\nVIP2.ALIDNS.COM\n', 'hostNames': ['VIP1.ALIDNS.COM', 'VIP2.ALIDNS.COM'], 'ips': []}, 'status': 'ok', 'rawText': 'Domain Name: tjhzyl.com\nRegistry Domain ID: 2611248516_DOMAIN_COM-VRSN\nRegistrar WHOIS Server: grs-whois.hichina.com\nRegistrar URL: http://whois.aliyun.com\nUpdated Date: 2021-05-11T03:41:17Z\nCreation Date: 2021-05-11T03:23:02Z\nRegistrar Registration Expiration Date: 2026-05-11T03:23:02Z\nRegistrar: Alibaba Cloud Computing (Beijing) Co., Ltd.\nRegistrar IANA ID: 420\nReseller:\nDomain Status: ok https://icann.org/epp#ok\nRegistrant City: \nRegistrant State/Province: tian jin\nRegistrant Country: CN\nRegistrant Email:https://whois.aliyun.com/whois/whoisForm\nRegistry Registrant ID: Not Available From Registry\nName Server: VIP1.ALIDNS.COM\nName Server: VIP2.ALIDNS.COM\nDNSSEC: unsigned\nRegistrar Abuse Contact Email: DomainAbuse@service.aliyun.com\nRegistrar Abuse Contact Phone: +86.95187\nURL of the ICANN WHOIS Data Problem Reporting System: http://wdprs.internic.net/\n>>>Last update of WHOIS database: 2021-09-27T02:07:48Z <<<\n\nFor more information on Whois status codes, please visit https://icann.org/epp\n\nImportant Reminder: Per ICANN 2013RAA`s request, Hichina has modified domain names`whois format of dot com/net/cc/tv, you could refer to section 1.4 posted by ICANN on http://www.icann.org/en/resources/registrars/raa/approved-with-specs-27jun13-en.htm#whois The data in this whois database is provided to you for information purposes only, that is, to assist you in obtaining information about or related to a domain name registration record. We make this information available "as is," and do not guarantee its accuracy. By submitting a whois query, you agree that you will use this data only for lawful purposes and that, under no circumstances will you use this data to: (1)enable high volume, automated, electronic processes that stress or load this whois database system providing you this information; or (2) allow, enable, or otherwise support the transmission of mass unsolicited, commercial advertising or solicitations via direct mail, electronic mail, or by telephone.  The compilation, repackaging, dissemination or other use of this data is expressly prohibited without prior written consent from us. We reserve the right to modify these terms at any time. By submitting this query, you agree to abide by these terms.For complete domain details go to:http://whois.aliyun.com/whois/domain/hichina.com', 'parseCode': 1275, 'header': '', 'strippedText': 'Domain Name: tjhzyl.com\nRegistry Domain ID: 2611248516_DOMAIN_COM-VRSN\nRegistrar WHOIS Server: grs-whois.hichina.com\nRegistrar URL: http://whois.aliyun.com\nUpdated Date: 2021-05-11T03:41:17Z\nCreation Date: 2021-05-11T03:23:02Z\nRegistrar Registration Expiration Date: 2026-05-11T03:23:02Z\nRegistrar: Alibaba Cloud Computing (Beijing) Co., Ltd.\nRegistrar IANA ID: 420\nReseller:\nDomain Status: ok https://icann.org/epp#ok\nRegistrant City:\nRegistrant State/Province: tian jin\nRegistrant Country: CN\nRegistrant Email:https://whois.aliyun.com/whois/whoisForm\nRegistry Registrant ID: Not Available From Registry\nName Server: VIP1.ALIDNS.COM\nName Server: VIP2.ALIDNS.COM\nDNSSEC: unsigned\nRegistrar Abuse Contact Email: DomainAbuse@service.aliyun.com\nRegistrar Abuse Contact Phone: +86.95187\nURL of the ICANN WHOIS Data Problem Reporting System: http://wdprs.internic.net/\n>>>Last update of WHOIS database: 2021-09-27T02:07:48Z <<<\nFor more information on Whois status codes, please visit https://icann.org/epp\nImportant Reminder: Per ICANN 2013RAA`s request, Hichina has modified domain names`whois format of dot com/net/cc/tv, you could refer to section 1.4 posted by ICANN on http://www.icann.org/en/resources/registrars/raa/approved-with-specs-27jun13-en.htm#whois The data in this whois database is provided to you for information purposes only, that is, to assist you in obtaining information about or related to a domain name registration record. We make this information available "as is," and do not guarantee its accuracy. By submitting a whois query, you agree that you will use this data only for lawful purposes and that, under no circumstances will you use this data to: (1)enable high volume, automated, electronic processes that stress or load this whois database system providing you this information; or (2) allow, enable, or otherwise support the transmission of mass unsolicited, commercial advertising or solicitations via direct mail, electronic mail, or by telephone.  The compilation, repackaging, dissemination or other use of this data is expressly prohibited without prior written consent from us. We reserve the right to modify these terms at any time. By submitting this query, you agree to abide by these terms.For complete domain details go to:http://whois.aliyun.com/whois/domain/hichina.com\n', 'footer': '\n', 'audit': {'createdDate': '2021-09-27 02:07:49 UTC', 'updatedDate': '2021-09-27 02:07:49 UTC'}, 'customField1Name': 'RegistrarContactEmail', 'customField1Value': 'DomainAbuse@service.aliyun.com', 'registrarName': 'Alibaba Cloud Computing (Beijing) Co., Ltd.', 'registrarIANAID': '420', 'whoisServer': 'grs-whois.hichina.com', 'createdDateNormalized': '2021-05-11 03:23:02 UTC', 'updatedDateNormalized': '2021-05-11 03:41:17 UTC', 'expiresDateNormalized': '2026-05-11 03:23:02 UTC', 'customField2Name': 'RegistrarContactPhone', 'customField3Name': 'RegistrarURL', 'customField2Value': '+86.95187', 'customField3Value': 'http://whois.aliyun.com', 'registryData': {'createdDate': '2021-05-11T03:23:02Z', 'updatedDate': '2021-05-11T03:41:17Z', 'expiresDate': '2026-05-11T03:23:02Z', 'domainName': 'tjhzyl.com', 'nameServers': {'rawText': 'VIP1.ALIDNS.COM\nVIP2.ALIDNS.COM\n', 'hostNames': ['VIP1.ALIDNS.COM', 'VIP2.ALIDNS.COM'], 'ips': []}, 'status': 'ok', 'rawText': 'Domain Name: TJHZYL.COM\n   Registry Domain ID: 2611248516_DOMAIN_COM-VRSN\n   Registrar WHOIS Server: grs-whois.hichina.com\n   Registrar URL: http://www.net.cn\n   Updated Date: 2021-05-11T03:41:17Z\n   Creation Date: 2021-05-11T03:23:02Z\n   Registry Expiry Date: 2026-05-11T03:23:02Z\n   Registrar: Alibaba Cloud Computing (Beijing) Co., Ltd.\n   Registrar IANA ID: 420\n   Registrar Abuse Contact Email: DomainAbuse@service.aliyun.com\n   Registrar Abuse Contact Phone: +86.95187\n   Domain Status: ok https://icann.org/epp#ok\n   Name Server: VIP1.ALIDNS.COM\n   Name Server: VIP2.ALIDNS.COM\n   DNSSEC: unsigned\n   URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/\n>>> Last update of whois database: 2021-09-27T02:07:42Z <<<\n\nFor more information on Whois status codes, please visit https://icann.org/epp\n\nNOTICE: The expiration date displayed in this record is the date the\nregistrar\'s sponsorship of the domain name registration in the registry is\ncurrently set to expire. This date does not necessarily reflect the expiration\ndate of the domain name registrant\'s agreement with the sponsoring\nregistrar.  Users may consult the sponsoring registrar\'s Whois database to\nview the registrar\'s reported date of expiration for this registration.\n\nTERMS OF USE: You are not authorized to access or query our Whois\ndatabase through the use of electronic processes that are high-volume and\nautomated except as reasonably necessary to register domain names or\nmodify existing registrations; the Data in VeriSign Global Registry\nServices\' ("VeriSign") Whois database is provided by VeriSign for\ninformation purposes only, and to assist persons in obtaining information\nabout or related to a domain name registration record. VeriSign does not\nguarantee its accuracy. By submitting a Whois query, you agree to abide\nby the following terms of use: You agree that you may use this Data only\nfor lawful purposes and that under no circumstances will you use this Data\nto: (1) allow, enable, or otherwise support the transmission of mass\nunsolicited, commercial advertising or solicitations via e-mail, telephone,\nor facsimile; or (2) enable high volume, automated, electronic processes\nthat apply to VeriSign (or its computer systems). The compilation,\nrepackaging, dissemination or other use of this Data is expressly\nprohibited without the prior written consent of VeriSign. You agree not to\nuse electronic processes that are automated and high-volume to access or\nquery the Whois database except as reasonably necessary to register\ndomain names or modify existing registrations. VeriSign reserves the right\nto restrict your access to the Whois database in its sole discretion to ensure\noperational stability.  VeriSign may restrict or terminate your access to the\nWhois database for failure to abide by these terms of use. VeriSign\nreserves the right to modify these terms at any time.\n\nThe Registry database contains ONLY .COM, .NET, .EDU domains and\nRegistrars.', 'parseCode': 251, 'header': '', 'strippedText': 'Domain Name: TJHZYL.COM\nRegistry Domain ID: 2611248516_DOMAIN_COM-VRSN\nRegistrar WHOIS Server: grs-whois.hichina.com\nRegistrar URL: http://www.net.cn\nUpdated Date: 2021-05-11T03:41:17Z\nCreation Date: 2021-05-11T03:23:02Z\nRegistry Expiry Date: 2026-05-11T03:23:02Z\nRegistrar: Alibaba Cloud Computing (Beijing) Co., Ltd.\nRegistrar IANA ID: 420\nRegistrar Abuse Contact Email: DomainAbuse@service.aliyun.com\nRegistrar Abuse Contact Phone: +86.95187\nDomain Status: ok https://icann.org/epp#ok\nName Server: VIP1.ALIDNS.COM\nName Server: VIP2.ALIDNS.COM\nDNSSEC: unsigned\nURL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/\n>>> Last update of whois database: 2021-09-27T02:07:42Z <<<\nFor more information on Whois status codes, please visit https://icann.org/epp\nNOTICE: The expiration date displayed in this record is the date the\nregistrar\'s sponsorship of the domain name registration in the registry is\ncurrently set to expire. This date does not necessarily reflect the expiration\ndate of the domain name registrant\'s agreement with the sponsoring\nregistrar.  Users may consult the sponsoring registrar\'s Whois database to\nview the registrar\'s reported date of expiration for this registration.\nTERMS OF USE: You are not authorized to access or query our Whois\ndatabase through the use of electronic processes that are high-volume and\nautomated except as reasonably necessary to register domain names or\nmodify existing registrations; the Data in VeriSign Global Registry\nServices\' ("VeriSign") Whois database is provided by VeriSign for\ninformation purposes only, and to assist persons in obtaining information\nabout or related to a domain name registration record. VeriSign does not\nguarantee its accuracy. By submitting a Whois query, you agree to abide\nby the following terms of use: You agree that you may use this Data only\nfor lawful purposes and that under no circumstances will you use this Data\nto: (1) allow, enable, or otherwise support the transmission of mass\nunsolicited, commercial advertising or solicitations via e-mail, telephone,\nor facsimile; or (2) enable high volume, automated, electronic processes\nthat apply to VeriSign (or its computer systems). The compilation,\nrepackaging, dissemination or other use of this Data is expressly\nprohibited without the prior written consent of VeriSign. You agree not to\nuse electronic processes that are automated and high-volume to access or\nquery the Whois database except as reasonably necessary to register\ndomain names or modify existing registrations. VeriSign reserves the right\nto restrict your access to the Whois database in its sole discretion to ensure\noperational stability.  VeriSign may restrict or terminate your access to the\nWhois database for failure to abide by these terms of use. VeriSign\nreserves the right to modify these terms at any time.\nThe Registry database contains ONLY .COM, .NET, .EDU domains and\nRegistrars.\n', 'footer': '\n', 'audit': {'createdDate': '2021-09-27 02:07:48 UTC', 'updatedDate': '2021-09-27 02:07:48 UTC'}, 'customField1Name': 'RegistrarContactEmail', 'customField1Value': 'DomainAbuse@service.aliyun.com', 'registrarName': 'Alibaba Cloud Computing (Beijing) Co., Ltd.', 'registrarIANAID': '420', 'createdDateNormalized': '2021-05-11 03:23:02 UTC', 'updatedDateNormalized': '2021-05-11 03:41:17 UTC', 'expiresDateNormalized': '2026-05-11 03:23:02 UTC', 'customField2Name': 'RegistrarContactPhone', 'customField3Name': 'RegistrarURL', 'customField2Value': '+86.95187', 'customField3Value': 'http://www.net.cn', 'whoisServer': 'grs-whois.hichina.com'}, 'contactEmail': 'DomainAbuse@service.aliyun.com', 'domainNameExt': '.com', 'estimatedDomainAge': 138}}, 'whois_2': {'ip': '8.140.99.84', 'success': True, 'type': 'IPv4', 'continent': 'Asia', 'continent_code': 'AS', 'country': 'China', 'country_code': 'CN', 'country_flag': 'https://cdn.ipwhois.io/flags/cn.svg', 'country_capital': 'Beijing', 'country_phone': '+86', 'country_neighbours': 'LA,BT,TJ,KZ,MN,AF,NP,MM,KG,PK,KP,RU,VN,IN', 'region': 'Beijing', 'city': 'Beijing', 'latitude': 39.904211, 'longitude': 116.407395, 'asn': 'AS37963', 'org': 'Aliyun Computing Co.LTD', 'isp': 'Hangzhou Alibaba Advertising Co.,Ltd.', 'timezone': 'Asia/Shanghai', 'timezone_name': 'China Standard Time', 'timezone_dstOffset': 0, 'timezone_gmtOffset': 28800, 'timezone_gmt': 'GMT +8:00', 'currency': 'Chinese Yuan', 'currency_code': 'CNY', 'currency_symbol': '¥', 'currency_rates': 6.467, 'currency_plural': 'Chinese yuan', 'completed_requests': 16}}, 'whatweb': {'whatweb_1': [{'url': 'http://tjhzyl.com', 'technologies': [{'slug': 'core-js', 'name': 'core-js', 'versions': ['3.1.3'], 'trafficRank': 0, 'confirmedAt': 1632451912, 'categories': [{'id': 59, 'slug': 'javascript-libraries', 'name': 'JavaScript libraries'}]}, {'slug': 'periodic', 'name': 'Periodic', 'versions': [], 'trafficRank': 0, 'confirmedAt': 1632451912, 'categories': []}, {'slug': 'plyr', 'name': 'Plyr', 'versions': [], 'trafficRank': 0, 'confirmedAt': 1632451912, 'categories': [{'id': 14, 'slug': 'video-players', 'name': 'Video players'}]}, {'slug': 'jquery-ui', 'name': 'jQuery UI', 'versions': ['1.11.4'], 'trafficRank': 0, 'confirmedAt': 1632451912, 'categories': [{'id': 59, 'slug': 'javascript-libraries', 'name': 'JavaScript libraries'}]}, {'slug': 'zepto', 'name': 'Zepto', 'versions': [], 'trafficRank': 0, 'confirmedAt': 1632451912, 'categories': [{'id': 59, 'slug': 'javascript-libraries', 'name': 'JavaScript libraries'}]}, {'slug': 'swiper-slider', 'name': 'Swiper Slider', 'versions': [], 'trafficRank': 0, 'confirmedAt': 1632451912, 'categories': [{'id': 19, 'slug': 'miscellaneous', 'name': 'Miscellaneous'}]}, {'slug': 'gsap', 'name': 'GSAP', 'versions': ['1.18.0'], 'trafficRank': 0, 'confirmedAt': 1632451912, 'categories': [{'id': 12, 'slug': 'javascript-frameworks', 'name': 'JavaScript frameworks'}]}, {'slug': 'isotope', 'name': 'Isotope', 'versions': [], 'trafficRank': 0, 'confirmedAt': 1632451912, 'categories': [{'id': 59, 'slug': 'javascript-libraries', 'name': 'JavaScript libraries'}]}, {'slug': 'nginx', 'name': 'Nginx', 'versions': [], 'trafficRank': 0, 'confirmedAt': 1632451912, 'categories': [{'id': 22, 'slug': 'web-servers', 'name': 'Web servers'}, {'id': 64, 'slug': 'reverse-proxies', 'name': 'Reverse proxies'}]}, {'slug': 'bootstrap', 'name': 'Bootstrap', 'versions': ['4.1.1'], 'trafficRank': 0, 'confirmedAt': 1632451912, 'categories': [{'id': 66, 'slug': 'ui-frameworks', 'name': 'UI frameworks'}]}, {'slug': 'jquery', 'name': 'jQuery', 'versions': ['1.12.4'], 'trafficRank': 0, 'confirmedAt': 1632451912, 'categories': [{'id': 59, 'slug': 'javascript-libraries', 'name': 'JavaScript libraries'}]}, {'slug': 'modernizr', 'name': 'Modernizr', 'versions': ['3.6.0'], 'trafficRank': 0, 'confirmedAt': 1629859859, 'categories': [{'id': 59, 'slug': 'javascript-libraries', 'name': 'JavaScript libraries'}]}]}], 'whatweb_2': {'status': 99, 'Web Frameworks': ['Twitter Bootstrap', 'Bootstrap'], 'status_code': 200, 'address': '美国 科罗拉多州布隆菲尔德市Level 3通信股份有限公司', 'url': 'tjhzyl.com', 'ip': '8.140.99.84', 'CMS': '未知', 'Web Servers': ['Nginx']}}, 'dns': {'dns_1': {'DNSData': {'domainName': 'tjhzyl.com', 'types': [-1], 'dnsTypes': '_all', 'audit': {'createdDate': '2021-09-27 02:48:47 UTC', 'updatedDate': '2021-09-27 02:48:47 UTC'}, 'dnsRecords': [{'type': 1, 'dnsType': 'A', 'name': 'tjhzyl.com.', 'ttl': 300, 'rRsetType': 1, 'rawText': 'tjhzyl.com.\t\t300\tIN\tA\t8.140.99.84', 'address': '8.140.99.84'}, {'type': 2, 'dnsType': 'NS', 'name': 'tjhzyl.com.', 'additionalName': 'vip1.alidns.com.', 'ttl': 300, 'rRsetType': 2, 'rawText': 'tjhzyl.com.\t\t300\tIN\tNS\tvip1.alidns.com.', 'target': 'vip1.alidns.com.'}, {'type': 2, 'dnsType': 'NS', 'name': 'tjhzyl.com.', 'additionalName': 'vip2.alidns.com.', 'ttl': 300, 'rRsetType': 2, 'rawText': 'tjhzyl.com.\t\t300\tIN\tNS\tvip2.alidns.com.', 'target': 'vip2.alidns.com.'}, {'type': 6, 'dnsType': 'SOA', 'name': 'tjhzyl.com.', 'ttl': 300, 'rRsetType': 6, 'rawText': 'tjhzyl.com.\t\t300\tIN\tSOA\tvip1.alidns.com. hostmaster.hichina.com. 2021051111 3600 1200 86400 360', 'admin': 'hostmaster.hichina.com.', 'host': 'vip1.alidns.com.', 'expire': 86400, 'minimum': 360, 'refresh': 3600, 'retry': 1200, 'serial': 2021051111}]}}, 'dns_2': {'aResults': [{'ipAddress': '8.140.99.84'}], 'aaaaResults': [], 'aResultsForWww': [{'ipAddress': '8.140.99.84'}], 'aaaaResultsForWww': [], 'nsResults': [{'nameServer': 'vip2.alidns.com'}, {'nameServer': 'vip1.alidns.com'}], 'txtResults': [], 'mxResults': [], 'soaResult': {'expire': 86400, 'defaultTTL': 360, 'refresh': 3600, 'retry': 1200, 'serial': 2021051111, 'hostmasterEmail': 'hostmaster.hichina.com', 'primaryNameserver': 'vip1.alidns.com'}, 'processResponseTime': '46ms', 'domain': 'tjhzyl.com', 'requestType': 'ANY', 'warnings': []}}, 'subdomain': {'sub_1': [{'ip': '8.140.99.84', 'port': '443', 'tips': [], 'level': 1, 'title': '\r\n\t\t\t天津华中医疗\r\n\t\t', 'domain': 'tjhzyl.com', 'is_ats': True, 'is_pci': True, 'server': 'nginx', 'duration': 2, 'icon_url': 'https://static.myssl.com/icon/3e3456b4a2aee23c29d7f72c67493c91', 'level_str': 'A+', 'ip_location': '中国', 'evaluate_date': '2021-08-17T06:36:15Z', 'demotion_reason': [], 'ignore_trust_level': 'A+', 'meet_gm_double_cert_statndard': False}, {'ip': '8.140.99.84', 'port': '443', 'tips': [], 'level': 1, 'title': '\r\n\t\t\t天津华中医疗\r\n\t\t', 'domain': 'www.tjhzyl.com', 'is_ats': True, 'is_pci': True, 'server': 'nginx', 'duration': 3, 'icon_url': 'https://static.myssl.com/icon/3e3456b4a2aee23c29d7f72c67493c91', 'level_str': 'A+', 'ip_location': '中国', 'evaluate_date': '2021-09-01T19:03:32Z', 'demotion_reason': [], 'ignore_trust_level': 'A+', 'meet_gm_double_cert_statndard': False}, {'ip': '8.140.99.84', 'port': '443', 'tips': [], 'level': 1, 'title': 'redirect to https://sc.tjhzyl.com/web/home.php', 'domain': 'sc.tjhzyl.com', 'is_ats': True, 'is_pci': True, 'server': 'nginx', 'duration': 3, 'icon_url': '', 'level_str': 'A+', 'ip_location': '中国', 'evaluate_date': '2021-08-31T23:43:39Z', 'demotion_reason': [], 'ignore_trust_level': 'A+', 'meet_gm_double_cert_statndard': False}]}, 'cdn': {'cdn_1': {'info': '您查询的这个域名是直接解析的A记录,或者不能访问,并没有使用CDN加速服务!', 'secess': False}, 'cdn_2': [{'ip': '8.140.99.84', 'location': '中国'}]}, 'waf': 'no waf', 'jssl': {'jssl_1': ['sc.tjhzyl.com', 'tjhzyl.com', 'cw.tjhzyl.com', 'm.tjhzyl.com', 'www.tjhzyl.com']}, 'whoisreverse': 'whoisreverse error', 'jnmap': {'ports': {'8.140.99.84': {'osmatch': {}, 'ports': [{'protocol': 'tcp', 'portid': '21', 'state': 'filtered', 'reason': 'no-response', 'reason_ttl': '0', 'service': {'name': 'ftp', 'method': 'table', 'conf': '3'}, 'scripts': []}, {'protocol': 'tcp', 'portid': '22', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '128', 'service': {'name': 'ssh', 'method': 'table', 'conf': '3'}, 'scripts': []}, {'protocol': 'tcp', 'portid': '23', 'state': 'filtered', 'reason': 'no-response', 'reason_ttl': '0', 'service': {'name': 'telnet', 'method': 'table', 'conf': '3'}, 'scripts': []}, {'protocol': 'tcp', 'portid': '25', 'state': 'filtered', 'reason': 'no-response', 'reason_ttl': '0', 'service': {'name': 'smtp', 'method': 'table', 'conf': '3'}, 'scripts': []}, {'protocol': 'tcp', 'portid': '80', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '128', 'service': {'name': 'http', 'method': 'table', 'conf': '3'}, 'scripts': []}, {'protocol': 'tcp', 'portid': '110', 'state': 'filtered', 'reason': 'no-response', 'reason_ttl': '0', 'service': {'name': 'pop3', 'method': 'table', 'conf': '3'}, 'scripts': []}, {'protocol': 'tcp', 'portid': '139', 'state': 'filtered', 'reason': 'no-response', 'reason_ttl': '0', 'service': {'name': 'netbios-ssn', 'method': 'table', 'conf': '3'}, 'scripts': []}, {'protocol': 'tcp', 'portid': '443', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '128', 'service': {'name': 'https', 'method': 'table', 'conf': '3'}, 'scripts': []}, {'protocol': 'tcp', 'portid': '445', 'state': 'filtered', 'reason': 'no-response', 'reason_ttl': '0', 'service': {'name': 'microsoft-ds', 'method': 'table', 'conf': '3'}, 'scripts': []}, {'protocol': 'tcp', 'portid': '3389', 'state': 'filtered', 'reason': 'no-response', 'reason_ttl': '0', 'service': {'name': 'ms-wbt-server', 'method': 'table', 'conf': '3'}, 'scripts': []}], 'hostname': [{'name': 'tjhzyl.com', 'type': 'user'}], 'macaddress': None, 'state': {'state': 'up', 'reason': 'reset', 'reason_ttl': '128'}}, 'stats': {'scanner': 'nmap', 'args': '"C:/Program Files (x86)/Nmap/nmap.exe" -oX - --top-ports 10 tjhzyl.com', 'start': '1632710789', 'startstr': 'Mon Sep 27 10:46:29 2021', 'version': '7.92', 'xmloutputversion': '1.05'}, 'runtime': {'time': '1632710790', 'timestr': 'Mon Sep 27 10:46:30 2021', 'summary': 'Nmap done at Mon Sep 27 10:46:30 2021; 1 IP address (1 host up) scanned in 1.49 seconds', 'elapsed': '1.49', 'exit': 'success'}}, 'os': {'error': True, 'msg': 'You must be root/administrator to continue!'}}}

raw_res = raw('tjhzyl.com', test_data)
# if raw_res != -1:
#     # 正常
#     print(raw_res)
#     pass
# else:
#     # 异常
#     pass
