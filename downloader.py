import urllib.request
import feedparser
import datetime
from raw_page import RawPageData


def download_html(url):
    '''
    This method get a URL and download the web page as HTML file
    
    :param url: URL to the web page as string
    :return: HTML code as string
    '''
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        charset = response.info().get_content_charset()
        page = response.read().decode(charset)
        statuscode= response.getcode()
        header = response.getheaders()
    return RawPageData(url, datetime.datetime.now(), "http", statuscode, header, page)


def download_rss(url):
    '''
    This method gets a URL and downloads the web page as XML file
    
    :param url: URL to the web page as string
    :return: XML file as string
    '''
    feed = feedparser.parse(url)
    return RawPageData(url, datetime.datetime.now(), "rss", feed.status, feed.headers, feed.entries)


