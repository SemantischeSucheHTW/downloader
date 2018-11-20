class Scheduler:
 
    def __init__(self, urlFilePath):
        pass

    '''
    This method gets a URL and puts it in the queue
    :param url: URL to a page as string
    '''
    def putURL(self, urlFilePath):
        pass
        
    '''
    This method returns the URL scheduled next
    :return: URL to a page as string
    '''
    def getURL(self):
        pass

    def isQueueEmpty(self):
        return self.queue.empty()

