import feedparser

def downloadPage(givenURL):
    feed = feedparser.parse(givenURL)
    return feed
    
    
    