from queue import Queue
from scheduler.scheduler import Scheduler

class BasicScheduler(Scheduler):
    
    def __init__(self, urlFilePath):
        self.queue = Queue()
         
        file = open(urlFilePath, "r") 
        for line in file:
            self.queue.put(line.rstrip())
        #print("loaded",self.queue.qsize(),"URLs")
        
    def putURL(self, url):
        self.queue.put(url)
        
    def getURL(self):
        return self.queue.get(block=True)
