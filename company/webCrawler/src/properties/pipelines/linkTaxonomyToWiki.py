'''
Created on Nov 28, 2018

@author: root

https://wikipedia-api.readthedocs.io/en/latest/
'''
import psycopg2
from urllib.parse import urlparse
import itertools

import wikipediaapi

class SQLConn(object):

    def open_spider(self, spider):
        if spider.name == 'tag':
            hostname = 'localhost'
            username = 'markus'
            password = 'markus' # your password
            database = 'webScraping'
            self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
            self.cur = self.connection.cursor()
            self.cur.execute("truncate taxonomy")

    def close_spider(self, spider):
        if spider.name == 'tag':
            self.cur.close()
            self.connection.close()

    def process_item(self, item, spider):
        '''
        identify spider make insert statement based on spider name
        '''
        if spider.name == 'tag':
            '''
            wordcloud link to wikipedia
            INSERT INTO public.taxonomy
                (terminology, wikiarticlename, wikiarticleurl)
                VALUES('', '', '');
            '''
            for i, (key, value) in enumerate(item.items()):
                for i in value:
                    list = i.split()
                    page_wiki = self.linkToWiki(term = list[0])
                    self.cur.execute("insert into taxonomy"
                                     "(terminology, wikiarticlename, wikiarticleurl)" 
                                     "values(%s,%s,%s)",(list[0], page_wiki.title, page_wiki.canonicalurl))
            self.connection.commit()
            return item
        else:
            return item      

    def linkToWiki(self, language = 'en', term = 'Python_(programming_language)'):
                
        wiki_wiki = wikipediaapi.Wikipedia(language)
        
        page_py = wiki_wiki.page(term)
        if term == None:
            page_py = wiki_wiki.page('Python_(programming_language)')
        
        if page_py.exists():
            print(page_py.fullurl)
            # https://en.wikipedia.org/wiki/Python_(programming_language)
            
            print(page_py.canonicalurl)
            # https://en.wikipedia.org/wiki/Python_(programming_language)
            return page_py        
        
        print("Page - Exists: %s" % page_py.exists())
        print("Page - Title: %s" % page_py.title)
        print("Page - Summary: %s" % page_py.summary[0:60])
        

        