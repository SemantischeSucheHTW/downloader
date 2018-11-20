class Downloader:

    '''
    Constructor
    :param scheduler: scheduler object from which URLs can be drawn
    :param mode: options: "html", "rss"
    :param database_interface: object, to which the downloaded data can be sent to
    '''
    def __init__(self, scheduler, mode, database_interface):
        pass

    def run(self):
        pass

    def download_html(url):
        '''
        This method gets an URL and download the web page as HTML file
        
        :param url: URL to the web page as string
        :return: HTML code as string
        '''
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            charset = response.info().get_content_charset()
            page = response.read().decode(charset)
            statuscode= response.getcode()
            header = response.getheaders()
        return RawPageData(url, datetime.datetime.now(), statuscode, header, page)
    
    
    def download_rss(url):
        '''
        This method gets an URL and downloads the web page as XML file
        
        :param url: URL to the web page as string
        :return: XML file as string
        '''
        feed = feedparser.parse(url)
        return RawPageData(url, datetime.datetime.now(), feed.status, feed.headers, feed.entries)

