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


def _send_cgi(rawrequests):
    jsonresponses = []
    for rawrequest in rawrequests:
        jsonrequest = json.dumps(rawrequest)
        req = urllib2.Request(url, jsonrequest)
        response = urllib2.urlopen(req)
        jsonresponse = response.read()
        jsonresponses.append(json.loads(jsonresponse))
    return jsonresponses


def test_getSupportedVersions():
    rawrequests = []
    rawrequests.append(
        {"apiVersion": "1.0", "method": "getSupportedVersions"})
    response = _send_cgi(rawrequests)[0]
    assert response['data']['apiVersions'][0] == '1.0'
    assert response['method'] == 'getSupportedVersions'


def test_addText():
    test_remove_all()
    rawrequests = []
    rawrequests.append({"apiVersion": "1.0", "method": "addText", "params": {"camera": 1, "text": "%F %T", "position": "0.27,-0.96",
                                                                             "textColor": "white", "textOLColor": "black", "textBGColor": "transparent", "fontSize": 80}})
    rawrequests.append({"apiVersion": "1.0", "method": "addText", "params": {"camera": 1, "text": "省级五个字\n地市五个字\n县市区五字\n乡镇五个字",
                                                                             "position": "0.65,0.3", "textColor": "white", "textOLColor": "black", "textBGColor": "transparent", "fontSize": 80}})
    rawrequests.append({"apiVersion": "1.0", "method": "addText", "params": {"camera": 1, "text": "一二三四五六七八九十一二三四五六\n",
                                                                             "position": "0,0.8", "textColor": "white", "textOLColor": "black", "textBGColor": "transparent", "fontSize": 80}})
    rawrequests.append({"apiVersion": "1.0", "method": "addText", "params": {"camera": 1, "text": "一二三四五六七八九十一二三四五\n",
                                                                             "position": "-0.95,0.8", "textColor": "white", "textOLColor": "black", "textBGColor": "transparent", "fontSize": 80}})
    response = _send_cgi(rawrequests)
    print response


def test_addImage():
    rawrequests = []


def test_list():
    rawrequests = []
    rawrequests.append(
        {"apiVersion": "1.0", "method": "list", "params": {}})
    response = _send_cgi(rawrequests)[0]
    assert response['apiVersion'] == '1.0'
    assert response['method'] == 'list'
    print response
    print response['data']


def test_remove(ids):
    rawrequests = []
    for id in ids:
        rawrequests.append({"apiVersion": "1.0", "method": "remove",
                            "params": {"identity": id}})
    response = _send_cgi(rawrequests)


def test_remove_all():
    test_remove(range(1, 5))


def test_setImage():
    rawrequests = []


def test_setText():
    rawrequests = []

# main
# test_getSupportedVersions()

# test_addText()
test_list()
# test_remove()
