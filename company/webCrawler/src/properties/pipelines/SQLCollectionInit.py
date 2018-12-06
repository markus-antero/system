'''
Created on Nov 30, 2018

@author: root
'''

import psycopg2
from urllib.parse import urlparse
import itertools

class SQLCollectInit(object):

    def open_spider(self, spider):
        if spider.name == 'init':    
            hostname = 'localhost'
            username = 'markus'
            password = 'markus' # your password
            database = 'webScraping'
            self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
            self.cur = self.connection.cursor()

    def close_spider(self, spider):
        if spider.name == 'init':
            self.cur.close()
            self.connection.close()

    def process_item(self, item, spider):
        '''
        identify spider make insert statement based on spider name
        '''
        if spider.name == 'init':
            '''
            INSERT INTO public.service
                (project, spider, servername, urlname, datetime)
                VALUES('', '', '', '', ''); 
            '''
            self.cur.execute("insert into service"
                             "(project, spider, servername, urlname, datetime)" 
                             "values(%s,%s,%s,%s,%s)",(item['project'],item['spider'],item['server'],item['url'],item['date']))
            self.connection.commit()
            return item
        else:
            return item