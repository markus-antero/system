# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from properties.items import UrlcollectorItem
from properties.items import PropertiesItem
from properties.items import Taxonomy
from properties.items import Blog

import datetime
import socket

class InitSpider(scrapy.Spider):
    name = 'init'
    allowed_domains = ['nedlaw.eu']
    start_urls = ['http://nedlaw.eu/']

    def parse(self, response):
        self.log("I am running")
        item = PropertiesItem()
            
        item['url']     = response.url
        item['project'] = self.settings.get('BOT_NAME')
        item['spider']  = self.name
        item['server']  = socket.gethostname()
        item['date']    = datetime.datetime.now()

        yield item

class UrlSpider(scrapy.Spider):
    name = 'url'
    allowed_domains = ['nedlaw.eu']
    start_urls = ['http://nedlaw.eu/']
    
    '''
    Main
        https://www.nedlaw.eu/

    Xpath Strings for nedlaw 
    '//a/text()
    
        xpath("//div[contains (@class, 'hs-menu')]/ul/li/a").extract()
        
        xpath("//div[contains (@class, 'hs-menu')]/ul/
                li[contains (@class, 'menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-2526')]
                /ul/li/a").extract()
    
        xpath("//div[contains (@class, 'hs-service-excerpt')]/h6/a//@href").extract()    

        xpath("//li[contains (@class, 'simple-links-item simple-links-widget-item')]/a//@href").extract()

        xpath("//div[contains (@class, 'tagcloud')]/a").extract()

    '''

    def parse(self, response):
        self.log("I am running")
        item = UrlcollectorItem()
        
        item['websiteTitle']      = response.xpath(
            "//div[contains(@class, 'hs-slide-cap-title animated fadeInLeft')]/span/descendant::text()").extract()
    
        item['externalURL']       = response.xpath(
            "//li[contains (@class, 'simple-links-item simple-links-widget-item')]/a//@href").extract()      
            
        item['InternalMenuURL']   = response.xpath(
            "//div[contains (@class, 'hs-menu')]/ul/li/a//@href").extract()

        item['InternalLinks']     = response.xpath(
            "//div[contains (@class, 'hs-service-excerpt')]/h6/a//@href").extract() 
        
        item['parentUrl']     = response.url
        
        yield item
        
    def genSources(self, xPathString):
        '''
        example xPath: 
            "//h2[contains(@class, 'title headline-font')]
            /a[contains(@class, 'campaign-link')]//@href"
        '''
    
class BlogSpider(scrapy.Spider):
    name = 'blog'
    allowed_domains = ['nedlaw.eu']
    start_urls = ['http://nedlaw.eu/blog']   
    
    '''
    Blog
        https://www.nedlaw.eu/blog/
        https://www.nedlaw.eu/blog/page/2/
        
    xpath 
        xpath("//div[contains (@class, 'content-area')]/article/div/a//@href").extract()
        xpath("//div[contains (@class, 'content-area')]/article/div/span[contains(@class, 'entry-date published updated')]").extract()

    '''
    npages = 6
    for i in range(2, npages + 2):
        start_urls.append("https://www.nedlaw.eu/blog/page/"+str(i)+"")
        
    def parse(self, response):
        self.log ('blog spider running')
        self.log (self.start_urls)
        
        for href in response.xpath("//div[contains (@class, 'content-area')]/article/div/a//@href"): 
            url  = href.extract() 
            yield scrapy.Request(url, callback=self.parse_dir_contents)    
        
            
    def parse_dir_contents(self, response):
        item = Blog()
        item['headLine']  = response.xpath("//h1[contains(@class, 'hs-main-title')]/descendant::text()").extract()
        item['sourceURL'] = response.url
        
        yield item
     
class TagSpider(scrapy.Spider):
    name = 'tag'
    allowed_domains = ['nedlaw.eu']
    start_urls = ['http://nedlaw.eu']            
    
    def parse(self, response):
        self.log("I am running") 
        
        item = Taxonomy()
        item['term']= response.xpath(
            "//div[contains (@class, 'tagcloud')]/a/@aria-label").extract()
        self.log(item)
        yield item

    '''
    tag
        https://www.nedlaw.eu/tag/
        https://www.nedlaw.eu/tag/tag_banking/
    
    Nedlaw 
        xpath("//div[contains (@class, 'tagcloud')]/a").extract()'
        xpath("//div[contains (@class, 'tagcloud')]/a/@aria-label").extract() 
        
    '''
    
    