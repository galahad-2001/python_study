# -*- coding: utf-8 -*-

import urllib2
import json

password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://192.168.77.169/"
password_mgr.add_password(None, top_level_url, "root", "pass")
handler = urllib2.HTTPDigestAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)
url = 'http://192.168.77.169/axis-cgi/dynamicoverlay/dynamicoverlay.cgi'
values = []
values.append({"apiVersion": "1.0", "method": "list", "params": {}})
# values.append({"apiVersion": "1.0", "method": "addText", "params": {"camera": 1, "text": "%F %T", "position": "0.27,-0.96",
#                                                                     "textColor": "white", "textOLColor": "black", "textBGColor": "transparent", "fontSize": 80}})
# values.append({"apiVersion": "1.0", "method": "addText", "params": {"camera": 1, "text": "省级五个字\n地市五个字\n县市区五字\n乡镇五个字",
#                                                                     "position": "0.65,0.3", "textColor": "white", "textOLColor": "black", "textBGColor": "transparent", "fontSize": 80}})
# values.append({"apiVersion": "1.0", "method": "addText", "params": {"camera": 1, "text": "一二三四五六七八九十一二三四五六\n",
#                                                                     "position": "0,0.8", "textColor": "white", "textOLColor": "black", "textBGColor": "transparent", "fontSize": 80}})
# values.append({"apiVersion": "1.0", "method": "addText", "params": {"camera": 1, "text": "一二三四五六七八九十一二三四五\n",
#                                                                     "position": "-0.95,0.8", "textColor": "white", "textOLColor": "black", "textBGColor": "transparent", "fontSize": 80}})
# values.append({"apiVersion": "1.0", "method": "remove",
#                "params": {"identity": 1}})
# values.append({"apiVersion": "1.0", "method": "remove",
#                "params": {"identity": 2}})
# values.append({"apiVersion": "1.0", "method": "remove",
#                "params": {"identity": 3}})
# values.append({"apiVersion": "1.0", "method": "remove",
#                "params": {"identity": 4}})

for value in values:
    data = json.dumps(value)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print json.loads(the_page)
