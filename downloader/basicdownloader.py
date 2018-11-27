from downloader.downloader import Downloader
from rawpagedata import RawPageData

class BasicDownloader(Downloader):

    def __init__(self, scheduler, mode, database_interface):
        self.scheduler = scheduler
        self.mode = mode
        self.database_interface = database_interface

    def run(self):
        while True:
            currentURL = self.scheduler.getURL()
            if (self.mode=="html"):
                data = self.download_html(currentURL)
            if (self.mode=="rss"):
                data = self.downloader_rss(currentURL)

            if data:
              print(f"Downloaded {currentURL}")
              self.database_interface.send(data)

