'''
Created on Nov 25, 2018

@author: root
'''

import scrapy
from scrapy.loader import ItemLoader

from properties.items import QuoteItem
from properties.items import PropertiesItem

import datetime
import socket

from properties.spiders import firstRun

class QuotesSpider(scrapy.Spider):
    name = "webCrawler"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        l = ItemLoader(item=PropertiesItem(), response=response)  
        
        for quote in response.css('div.quote'):
            item_content = quote.css('span.text::text').extract_first()
            item_author = quote.css('small.author::text').extract_first()
            quoteItem = QuoteItem(content= item_content,author=item_author)
            yield quoteItem

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        
        if firstRun:   
            l.add_value('url', response.url)
            l.add_value('project', self.settings.get('BOT_NAME'))
            l.add_value('spider', self.name)
            l.add_value('server', socket.gethostname())
            l.add_value('date', datetime.datetime.now())
            
            firstRun = False  
        
        return l.load_item()    
            
            
            