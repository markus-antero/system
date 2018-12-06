from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def main():
    '''
    available spiders:
        * init
        * url
        * blog 
        * tag
    '''    
    process = CrawlerProcess(get_project_settings())
    '''
    # quotes and author project
    process.crawl('webCrawler', domain='quotes.toscrape.com/')
    '''
#    process.crawl('init', domain='nedlaw.eu')
    
    process.crawl('url', domain='nedlaw.eu')
    
#    process.crawl('tag', domain='nedlaw.eu/')
    
#    process.crawl('blog', domain='nedlaw.eu')
    
    process.start() # the script will block here until the crawling is finished
    
if __name__ == '__main__':
    main()