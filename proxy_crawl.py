# coding=utf-8
# author=Alan Lee
# data=2018/3/28
import constants
import requests
import random
from page_parser import PageParser


if __name__ == '__main__':
    proxy_file = open(constants.PROXY_FILE, 'w')
    page_parser = PageParser.PageParser()
    for i in range(1, 100):

        proxy_url = constants.URL_FREE_PROXY + str(i)
        headers = {'User-Agent': random.choice(constants.USER_AGENT)}
        r = requests.get(proxy_url,
                         headers=headers)
        page_parser.set_html_doc(r.text)
        proxy_dict_list = page_parser.extract_proxy_urls()
        break


