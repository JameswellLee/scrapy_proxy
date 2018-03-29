# coding=utf-8
# author=Alan Lee
# data=2018/3/28
from bs4 import BeautifulSoup

class PageParser:
    """
    负责从html文档中解析视频实体信息

    当然了，你也可以使用Xpath表达式来提取。这里只是为了方便。
    """
    __soup = ''
    __movie = None
    __NOT_FOUND = u'页面不存在'
    __html_doc = ''

    def __set_bs_soup(self):

        self.__soup = BeautifulSoup(self.__html_doc, 'html.parser')

    def __is_404_page(self):

        if self.__html_doc.find(self.__NOT_FOUND) != -1:
            return True

        if len(self.__html_doc) < 500:
            return True

        return False

    def set_html_doc(self, html_doc):
        self.__html_doc = html_doc

    def extract_proxy_urls(self):
        """
        如果为404或其他出错页面，返回None。
        :return: None|dict
        """

        if self.__html_doc is None:
            return []

        if self.__is_404_page():
            return []
        self.__set_bs_soup()
        proxy_dict_list = []
        trs = self.__soup.find_all('tr')
        for i in range(1, len(trs)):
            tds = trs[i].find_all('td')
            ip = tds[1].text
            port = tds[2].text
            type = tds[5].text
            proxt_dict = {'ip': ip,
                          'port': port,
                          'type': type}
            print(proxt_dict)
        return proxy_dict_list