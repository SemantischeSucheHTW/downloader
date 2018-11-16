import urllib.request
import feedparser


def download_html(url):
    '''
    This method get a URL and download the web page as HTML file
    
    :param url: URL to the web page as string
    :return: HTML code as string
    '''
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        page = response.read()
    return page


def download_rss(url):
    '''
    This method gets a URL and downloads the web page as XML file
    
    :param url: URL to the web page as string
    :return: XML file as string
    '''
    feed = feedparser.parse(url)
    return feed


