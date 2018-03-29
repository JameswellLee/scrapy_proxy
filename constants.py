# coding=utf-8
# author=Alan Lee
# data=2018/3/28 

PROXY_FILE = 'proxy.txt'
URL_FREE_PROXY = 'http://www.xicidaili.com/wn/'


# 搜索引擎（SEO爬虫）的请求头
USER_AGENT = [
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)',
        'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)',
        'DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)',
        'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
        'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
        'ia_archiver (+http://www.alexa.com/site/help/webmasters; crawler@alexa.com)'
    ]
CHECK_PROXY_TIME_OUT = 1
THREAD_NUM = 8

