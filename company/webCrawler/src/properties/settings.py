# Scrapy settings for properties project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

#BOT_NAME = 'properties
BOT_NAME = 'webCrawler'

SPIDER_MODULES = ['properties.spiders']
NEWSPIDER_MODULE = 'properties.spiders'

# Crawl responsibly by identifying yourself (and your website) on
# the user-agent
#USER_AGENT = 'properties (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'properties.pipelines.SQLCollectionInit.SQLCollectInit': 200,
    'properties.pipelines.sqlCollectURLs.ConnURLs': 250,
    'properties.pipelines.linkTaxonomyToWiki.SQLConn': 275,
    'properties.pipelines.sqlConnection.postgreConn': 300,
    #'properties.pipelines.tidyup.TidyUp': 100,
    'properties.pipelines.es.EsWriter': 800,
    #'properties.pipelines.geo.GeoPipeline': 400,
    
}

EXTENSIONS = {'properties.latencies.Latencies': 500, }
LATENCIES_INTERVAL = 5

ES_PIPELINE_URL = 'http://es:9200/properties/property/'

LOG_LEVEL = "INFO"

# Disable S3
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
