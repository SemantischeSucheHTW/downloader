import datetime
import feedparser
import urllib.request

from downloader import Downloader
from raw_page import RawPageData

class BasicDownloader(Downloader):

    def __init__(self, scheduler, mode, database_interface):
        self.scheduler = scheduler
        self.mode = mode
        self.database_interface = database_interface

    #simply downloads all urls from the scheduler queue and then terminates
    def run(self):
        while (not scheduler.isQueueEmpty()):
            currentURL = scheduler.getURL
            if (self.mode=="html"):
                data = download_html(currentURL)
            if (self.mode=="rss"):
                data = downloader_rss(currentURL)
            self.database_interface.send(data)

