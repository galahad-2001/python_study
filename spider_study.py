# -*- coding: utf-8 -*-

import urllib2
import numpy as np
from bs4 import BeautifulSoup

# Some User Agents
hds = [{'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
       {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
       {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]


def get_source_code(url):
    req = urllib2.Request(url)
    source_code = urllib2.urlopen(req).read()
    return source_code


def get_subject_items(source_code):
    soup = BeautifulSoup(source_code, "html.parser")
    subject_list = soup.find('ul', {'class': 'subject-list'})
    subject_items = subject_list.findAll('li', {'class': 'subject-item'})
    return subject_items


def get_list_subject_items(subject_items):
    list_subject_items = []
    for subject_item in subject_items:
        title = subject_item.find('div', {'class': 'info'}).a.get_text().strip().replace(' ', '').replace('\n', '')
        pub = subject_item.find('div', {'class': 'pub'}).get_text().strip()
        rating_nums = subject_item.find('span', {'class': 'rating_nums'}).get_text().strip()
        pl = subject_item.find('span', {'class': 'pl'}).get_text().strip().strip('(').strip(u'人评价)')
        p = subject_item.p.get_text().strip().replace('\n', '')
        print title
        print pub
        print rating_nums
        print pl
        print p
        print '*' * 50
        list_subject_items.append([title, pub, rating_nums, rating_nums, p])
    return list_subject_items


if __name__ == '__main__':
    i = 0
    while i <= 1:
        url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=' + str(i) + '&type=T'
        # print url
        print get_list_subject_items(get_subject_items(get_source_code(url)))
        i += 20
