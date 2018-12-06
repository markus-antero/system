'''
Created on Nov 25, 2018

@author: root
'''

import psycopg2
from urllib.parse import urlparse
import itertools
import datetime

class postgreConn(object):

    def open_spider(self, spider):
        if spider.name == 'webCrawler' or spider.name == 'blog':
            hostname = 'localhost'
            username = 'markus'
            password = 'markus' # your password
            database = 'webScraping'
            self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
            self.cur = self.connection.cursor()
            self.cur.execute("truncate blog")

    def close_spider(self, spider):
        if spider.name == 'webCrawler' or spider.name == 'blog':
            self.cur.close()
            self.connection.close()

    def process_item(self, item, spider):
        '''
        identify spider make insert statement based on spider name
        '''
        if spider.name == 'webCrawler':
            self.cur.execute("truncate quotes_content")
            self.cur.execute("insert into quotes_content(content,author) values(%s,%s)",(item['content'],item['author']))
            self.connection.commit()
            return item
               
        elif spider.name == 'blog':
            '''
            INSERT INTO public.blog
                (headline, published, author, url, keywords)
                VALUES('', '', '', '', '');
                
            headLine           = Field()
            sourceURL          = Field()
            '''                 
            min = item["sourceURL"]
            list = min.split('/')
            print (list[3],list[4],list[5])
            author = 'Markus' 
            published = datetime.datetime (int(list[3]),int(list[4]),int(list[5]))
            
            self.cur.execute("insert into blog"
                             " (headline, published, author, url)"
                             " values(%s,%s,%s,%s)",(item['headLine'],published, author, item['sourceURL']))
            self.connection.commit()
            return item
        
        else:
            return item
    
    
    