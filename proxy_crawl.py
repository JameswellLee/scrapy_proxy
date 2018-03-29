# coding=utf-8
# author=Alan Lee
# data=2018/3/28
import constants
import requests
import random
import json
import utils
import multiprocessing as mp
from page_parser import PageParser


def crawl_prxxy_by_pages(page_urls, queue):
    page_parser = PageParser.PageParser()
    for page_url in page_urls:
        headers = {'User-Agent': random.choice(constants.USER_AGENT)}
        r = requests.get(page_url,
                         headers=headers)
        page_parser.set_html_doc(r.text)
        proxy_dict_list = page_parser.extract_proxy_urls()
        for proxy_dict in proxy_dict_list:
            if utils.check_https_proxy(proxy_dict):
                print('crawled a valid proxy:%s' % utils.format_proxy_dict(proxy_dict))
                queue.put(proxy_dict)


def run_func(args):
    crawl_prxxy_by_pages(args[0], args[1])

if __name__ == '__main__':
    proxy_file = open(constants.PROXY_FILE, 'w')
    m = mp.Manager()
    valid_proxy_queue = m.Queue()
    thread_nums = constants.THREAD_NUM
    pool = mp.Pool(thread_nums)
    pages_urls = []
    for i in range(1, 100):
        proxy_url = constants.URL_FREE_PROXY + str(i)
        pages_urls.append(proxy_url)

    args = []
    add_count = int(len(pages_urls) / thread_nums)
    for i in range(thread_nums):
        if i < thread_nums - 1:
            args.append((pages_urls[i * add_count: (i+1)*add_count], valid_proxy_queue))
        else:
            args.append((pages_urls[i * add_count: len(pages_urls)], valid_proxy_queue))
    pool.map(run_func, args)
    pool.close()
    pool.join()
    while not valid_proxy_queue.empty():
        proxy_file.write(valid_proxy_queue.get() + '\n')
        proxy_file.flush()







