'''
Created on Nov 30, 2018

@author: root
'''
import psycopg2
from urllib.parse import urlparse
import itertools
import pandas as pd
import re
import json
import urllib.request
import socket

class ConnURLs(object):

    '''
    URL + domain
        INSERT INTO public."domainLocation"
        (url, title, classifier, "domain", classifiertxt)
        VALUES('', '', 0, '', '');
                
        UrlcollectorItem: {
           'InternalLinks': ['https://www.nedlaw.eu/development/',
                
           'InternalMenuURL': ['https://www.nedlaw.eu/#hs-about-us-section',
                
           'externalURL': ['https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/', 
           
        https://ipinfo.info/html/ip_checker.php  
    '''
    def open_spider(self, spider):
        if spider.name == 'url':
            hostname = 'localhost'
            username = 'markus'
            password = 'markus' # your password
            database = 'webScraping'
            self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
            self.cur = self.connection.cursor()
            self.cur.execute("truncate public.\"domainLocation\"")

    def close_spider(self, spider):
        if spider.name == 'url':
            '''
            Query the selected addresses at domain field 
                Make the domain field include the protocol
                Use distinct
            
            get geo stats 
            insert to organization table
            '''
            self.cur.execute('SELECT distinct "domain", parenturl FROM public."domainLocation";')
            domains = self.cur.fetchall()
            for domain in domains:
                self.testIP(host = domain[0])
                
            self.cur.close()
            self.connection.close()
    
    def process_item(self, item, spider):
        '''
        identify spider make insert statement based on spider name
        '''
        if spider.name == 'url':
            
            title = item['websiteTitle']
            parentDomain = item['parentUrl']
            
            for i, (key, value) in enumerate(item.items()):
                print(key, ' corresponds to: ', value)
                print (i)    
                if key == 'externalURL':
                    print (value)
                    classifier = 1
                    classifierTxt = 'external'
                    for i in value:
                        parsed_uri = urlparse(i)
                        result_domain = '{uri.netloc}'.format(uri=parsed_uri)
                        self.cur.execute("insert into public.\"domainLocation\""
                                 "(url, title, classifier, \"domain\", classifiertxt, parenturl)"
                                 "values(%s,%s,%s,%s,%s,%s)",(i,title, classifier,result_domain,classifierTxt, parentDomain))
                    
                elif key == 'InternalMenuURL':
                    print (value)
                    classifier = 2
                    classifierTxt = 'internal'
                    for i in value:
                        parsed_uri = urlparse(i)
                        result_domain = '{uri.netloc}'.format(uri=parsed_uri)
                        self.cur.execute("insert into public.\"domainLocation\""
                                 "(url, title, classifier, \"domain\", classifiertxt, parenturl)"
                                 "values(%s,%s,%s,%s,%s,%s)",(i,title, classifier,result_domain,classifierTxt, parentDomain))
                    
                elif key == 'InternalLinks':
                    print (value)
                    classifier = 2
                    classifierTxt = 'internal'
                    for i in value:
                        parsed_uri = urlparse(i)
                        result_domain = '{uri.netloc}'.format(uri=parsed_uri)
                        self.cur.execute("insert into public.\"domainLocation\""
                                 "(url, title, classifier, \"domain\", classifiertxt, parenturl)"
                                 "values(%s,%s,%s,%s,%s,%s)",(i,title, classifier,result_domain,classifierTxt, parentDomain))
            
            self.connection.commit() 
            return item
        
        else:
            return item
        
    def testIP(self, host = 'www.google.com'):
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
        #hostname = data['hostname']    
        
        self.cur.execute('INSERT INTO public.organization'
                        '("domain", ip, organization, country, city, region, "location")'
                        'VALUES(%s,%s,%s,%s,%s,%s,%s);', (host, IP, org,country,city,region,location))
        self.connection.commit() 
        
        
        
        
        
        
        
        
        
        
    