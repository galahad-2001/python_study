# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup


if __name__ == '__main__':

    url = 'https://cst.axis.com/'
    req = urllib2.Request(url)
    the_page = urllib2.urlopen(req)
    source_code = the_page.read()
    print source_code
    # print get_source_code(url)
