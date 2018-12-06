'''
Created on Nov 26, 2018

@author: root
'''

import re
import json
import urllib.request
import socket

def testIP(host = 'www.google.com'):
    url   = 'http://ipinfo.io/'
    token = '8aa18db8474695'
    ip    = socket.gethostbyname(host)
    
    DNSsearch = url + ip + '/json?token=' + token
    
    req = urllib.request.Request(DNSsearch)
    with urllib.request.urlopen(req) as response:
       data = json.load(response)
    
    IP       = data['ip']
    org      = data['org']
    city     = data['city']
    country  = data['country']
    region   = data['region']
    location = data['loc']
    hostname = data['hostname']
    
    print ('Your IP detail\n ')
    print ('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))
    print ('Hostname : {0} \nLocation : {1}'.format(hostname,location))


if __name__ == '__main__':
    testIP(host = 'arachnoid.com')