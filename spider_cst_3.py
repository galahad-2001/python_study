#!/usr/bin/python3

import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup
import re
import time
import sys
import xlwt


def spider_cst_read_only():
    '''
    This is a spider for fetching cst tickets which region belong to China
    '''

    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    top_level_url = "https://cst.axis.com/"
    password_mgr.add_password(None, top_level_url, "username", "password")
    # handler = urllib2.HTTPDigestAuthHandler(password_mgr)
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(handler)
    urllib.request.install_opener(opener)

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('CST')
    title_list = ['Ticket_ID', 'Description', 'Product', 'Customer',
                  'CustomerCompany', 'State', 'StateInfo', 'Age', 'Waited']
    for i in range(len(title_list)):
        ws.write(0, i, title_list[i])

    page = 1

    while True:
        url = 'https://cst.axis.com/?LM_search_page=' + \
            str(page) + '&view=search&search=1&product_category=any&region_id=17&ts_method=exact&ts_txt=on&escalated=Any&state=Any&file=Any&workflow_id=any&date_from=2016-05-31&date_to=2018-05-31&customer_email=on&customer_cmp=on&p=-'
        req = urllib.request.Request(url)
        the_page = urllib.request.urlopen(req)
        source_code = the_page.read()
        # print source_code

        soup = BeautifulSoup(source_code, "html.parser")
        p = re.compile(r'search_\d\d?_\d\d?$')
        subject_lists = soup.findAll('tr', {'id': p})

        if (len(subject_lists) == 0):
            print('%d results found!' % count)
            break

        print('Fetching page %d, please wait...' % page)

        count = 50 * (page - 1) + 1

        for subject_list in subject_lists:
            # print subject_list
            subject_items = subject_list.findAll('td', {'valign': 'top'})
            Ticket_ID = subject_items[0].get_text().strip()
            Description = subject_items[2].get_text().strip()
            Product = subject_items[3].get_text().strip()
            Customer = subject_items[4].span.get_text().strip()
            CustomerCompany = subject_items[4].get_text().strip(
            )[len(Customer):]  # New method to get CustomerCompany
            State = subject_items[5].span.get_text().strip()
            StateInfo = subject_items[5].get_text(
            ).strip().lstrip(State).strip('@')
            Age = subject_items[6].get_text().strip().strip(
                ' days').strip(' day')
            Waited = subject_items[7].get_text(
            ).strip().strip(' days').strip(' day')
            text_list = [Ticket_ID, Description, Product, Customer,
                         CustomerCompany, State, StateInfo, Age, Waited]
            # print "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (Ticket_ID, Description, Product, Customer, CustomerCompany, State, StateInfo, Age, Waited)

            for i in range(len(text_list)):
                ws.write(count, i, text_list[i])
            count += 1

        if (count < (50 * page + 1)):
            print('%d results found!' % count)
            break

        # break # for test
        page += 1

    wb.save('../spider_results/CST_Spider_%s.xls' %
            (time.strftime("%Y%m%d_%H%M%S", time.localtime())))


if __name__ == '__main__':
    spider_cst_read_only()
