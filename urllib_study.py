import urllib2
import json

password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://192.168.77.169/"
password_mgr.add_password(None, top_level_url, "root", "pass")
handler = urllib2.HTTPDigestAuthHandler(password_mgr)
opener = urllib2.build_opener(handler) 
a_url = 'http://192.168.77.169/'  
opener.open(a_url)  
# urllib2.install_opener(opener) 

# request = urllib2.urlopen('http://192.168.77.169/axis-cgi/param.cgi?action=list')
# data = request.read()
# print data