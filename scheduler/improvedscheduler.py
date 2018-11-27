from queue import Queue
from scheduler import Scheduler

import datetime
import threading

class ImprovedScheduler(Scheduler):

    def __init__(self, urlfilepath, pagemetadata_agent, initialpage, initialpage_backoffseconds):
        self.queue = Queue()
        self.pagemetadata_agent = pagemetadata_agent
        self.initialpage = initialpage
        self.initialpage_backoffseconds = initialpage_backoffseconds
        self.queued_urls = set()

        file = open(urlfilepath, "r")
        lines = file.read().splitlines()

        for line in lines:
            self.queued_urls.add(line)
            self.queue.put(line.rstrip())

    def putURL(self, url):
        print(f"{url} is to be queued")
        if url not in self.queued_urls:
          last_downloadtime = self.pagemetadata_agent.getLastDownloadTime(url)

          if not last_downloadtime:
              print(f"Queueing {url}")
              self.queue.put(url)
              self.queued_urls.add(url)
              return
          else:
              print(f"last_downloadtime for {url} found. Not queueing")

          if url == self.initialpage:
              if (datetime.datetime.now() - last_downloadtime).seconds > self.initialpage_backoffseconds:
                  print(f"Queueing {url}")
                  self.queue.put(url)
                  self.queued_urls.add(url)
        else:
          print(f"{url} is already queued")

    def getURL(self):
        url = self.queue.get()
        self.queued_urls.remove(url)
        return url 
