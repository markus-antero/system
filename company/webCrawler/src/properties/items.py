from scrapy.item import Item, Field
import pandas as pd

class PropertiesItem(Item):
    '''
    Meta data, records, who did, what, when
    Usage:
    Header
        from scrapy.loader import ItemLoader
        
    Code
        @ def parse_item(self, response):    
            
            l = ItemLoader(item=PropertiesItem(), response=response)
            ...
            l.add_value('url', response.url)
            ...
            return l.load_item()
    '''
    # Housekeeping fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()


class QuoteItem(Item):
    '''
    Collects quotes and names, test case
    spider name = 'webCrawler'
    '''
    content = Field()
    author = Field()
    
class Taxonomy (Item):
    '''
    Linking wikipedia to popular terms
    spider name = 'tag'
    
    linkToWikipedia: link, headline, ...    
    '''
    term               = Field()
    linkToWikipedia    = pd.DataFrame()
    
class Blog (Item):
    '''
    Linking wikipedia to popular terms
    spider name = 'tag'
    
    linkToWikipedia: link, headline, ...    
    '''
    headLine           = Field()
    sourceURL          = Field()
   
    
class UrlcollectorItem(Item):
    websiteTitle      = Field()      # Id field
    
    externalURL       = Field()      # Id field
    InternalMenuURL   = Field()      # Website URL 
    InternalLinks     = Field()      # Website container
    parentUrl         = Field()
    
class Profile(Item):
    linkedInProfile   = Field()      # Linked -in profile 
    TwitterProfile    = Field()      # Twitter handle 
    
    hostName          = ''
    hostEmail         = ''
    phone             = ''    
    