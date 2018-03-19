# -*- coding: utf-8 -*-

import urllib2
import numpy as np
from bs4 import BeautifulSoup

# Some User Agents
hds = [{'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
       {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
       {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'
req = urllib2.Request(url)
source_code = urllib2.urlopen(req).read()
plain_text = str(source_code)
soup = BeautifulSoup(plain_text, "html.parser")
list_soup = soup.find('ul', {'class': 'subject-list'})
list_soup_books = soup.findAll('li', {'class': 'subject-item'})

for list_soup_book in list_soup_books:
    info = list_soup_book.find('div', {'class': 'info'})
    pub = list_soup_book.find('div', {'class': 'pub'})
    print info
    print '*' * 50
    print pub
    print '*' * 150
