from datetime import datetime
from urllib.parse import urlparse

# gives
'http://stackoverflow.com/'

class TidyUp(object):
    """A pipeline that does some basic post-processing"""

    def process_item(self, item, spider):
        """
        Pipeline's main method. Formats the date as a string.
        """

        item['date'] = map(datetime.isoformat, item['date'])

        return item

    def getDomain(self, url):
        '''
        {uri.netloc} equals domain
        
        available values: https://pymotw.com/2/urlparse/
            http://user:pass@NetLoc:80/path;parameters?query=argument#fragment'
                scheme  : http
                netloc  : user:pass@NetLoc:80
                path    : /path
                params  : parameters
                query   : query=argument
                fragment: fragment
                username: user
                password: pass
                hostname: netloc (netloc in lower case)
                port    : 80
        '''
        parsed_uri = urlparse(url)
        result_ip = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        result_domain = '{uri.netloc}'.format(uri=parsed_uri)
        print(result_domain)

'''
import tldextract
tldextract.extract('http://forums.news.cnn.com/')
tldextract.extract('http://forums.bbc.co.uk/') # United Kingdom
tldextract.extract('http://www.worldbank.org.kg/') # Kyrgyzstan
'''