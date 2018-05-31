# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import re
import time
import sys


if __name__ == '__main__':

    reload(sys)
    sys.setdefaultencoding('utf-8')

    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    top_level_url = "https://cst.axis.com/"
    password_mgr.add_password(None, top_level_url, "jayden", "Wangwenyan2017")
    # handler = urllib2.HTTPDigestAuthHandler(password_mgr)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)

    url = 'https://cst.axis.com/?LM_search_page=1&view=search&search=1&product_category=any&region_id=17&ts_method=exact&ts_txt=on&escalated=Any&state=Any&file=Any&workflow_id=any&date_from=2016-05-31&date_to=2018-05-31&customer_email=on&customer_cmp=on&p=-'
    req = urllib2.Request(url)
    the_page = urllib2.urlopen(req)
    source_code = the_page.read()
    # print source_code

    f = open('CST_Spider_%s.txt' % (time.strftime("%Y%m%d_%H%M%S", time.localtime())), 'w')
    print >> f, "Ticket_ID,Description,Product,Customer,CustomerCompany,State,StateInfo,Age,Waited"

    soup = BeautifulSoup(source_code, "html.parser")
    p = re.compile(r'search_\d\d?_\d\d?$')
    subject_lists = soup.findAll('tr', {'id': p})
    for subject_list in subject_lists:
        # print subject_list
        # print '*' * 100
        items_list = []
        subject_items = subject_list.findAll('td', {'valign': 'top'})
        Ticket_ID = subject_items[0].get_text().strip()
        Description = subject_items[2].get_text().strip().replace(',', ' ').replace('，', ' ')
        Product = subject_items[3].get_text().strip()
        Customer = subject_items[4].span.get_text().strip()
        CustomerCompany = subject_items[4].get_text().strip().strip(Customer)
        State = subject_items[5].span.get_text().strip().replace(',', ' ').replace('，', ' ')
        StateInfo = subject_items[5].get_text().strip().strip(State)
        Age = subject_items[6].get_text().strip().strip(' days').strip(' day')
        Waited = subject_items[7].get_text().strip().strip(' days').strip(' day')
        # print "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (Ticket_ID, Description, Product, Customer, CustomerCompany, State, StateInfo, Age, Waited)
        print >> f, "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (Ticket_ID, Description, Product, Customer, CustomerCompany, State, StateInfo, Age, Waited)
        # break

    f.close()
