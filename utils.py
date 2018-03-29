# coding=utf-8
# author=Alan Lee
# data=2018/3/29 
import requests
import constants
import random


def test(ip, port, type='https'):
    proxy_dict = {
        'ip':ip,
        'port':port,
        'type':type
    }
    return check_https_proxy(proxy_dict)


def check_https_proxy(proxy_dict):
    try:
        if proxy_dict['type'] == 'http':
            return False
        test_url_dict = {
            'https': 'https://www.douban.com/'
        }
        headers = {'User-Agent': random.choice(constants.USER_AGENT)}
        proxy_url = format_proxy_dict(proxy_dict)
        print(proxy_url)
        proxy = {proxy_dict['type']:proxy_url}
        r = requests.get(test_url_dict[proxy_dict['type']],
                         headers=headers,
                         proxies=proxy,
                         timeout=constants.CHECK_PROXY_TIME_OUT)
        print(r)
        return '豆瓣' in r.text
    except:
        return False


def format_proxy_dict(proxy_dict):
    proxy_url = '%s://%s:%s' % (proxy_dict['type'], proxy_dict['ip'], proxy_dict['port'])
    return proxy_url

if __name__ == '__main__':
    test('119.28.50.37', '82')
