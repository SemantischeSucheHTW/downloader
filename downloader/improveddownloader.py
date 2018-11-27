from downloader import Downloader
from threading import Thread

import time

class ImprovedDownloader(Downloader):

    def __init__(self, scheduler, database_interface, mode, sleep_time):
        self.scheduler = scheduler
        self.database_interface = database_interface
        self.mode = mode
        self.sleep_time = sleep_time

    def _run_loop(self):
      while True:
          currentURL = self.scheduler.getURL()
          print(currentURL)
          if self.mode=="html":
              data = self.download_html(currentURL)
          if self.mode=="rss":
              data = self.download_rss(currentURL)

          if data:
            print(f"Downloaded {currentURL}")
            self.database_interface.send(data)
            time.sleep(self.sleep_time)

    def run(self):
        Thread(target=lambda: self._run_loop()).start()
