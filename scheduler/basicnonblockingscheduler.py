from threading import Thread

class BasicNonBlockingScheduler(Scheduler):
    
    def __init__(self, urlFilePath):
        self.queue = Queue()
         
        file = open(urlFilePath, "r") 
        for line in file:
            self.queue.put(line)
        #print("loaded",self.queue.qsize(),"URLs")
        
    def putURL(self, url):
        #self.queue.put(url)
        Thread(target=lambda x: self.queue.put(x), args=url)
        
    #def get():
    #    return self.queue.get()
        
    def getURL(self):
        #Thread(target=lambda: get(), args=None)
        return self.queue.get()
