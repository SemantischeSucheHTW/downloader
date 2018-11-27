from pymongo import MongoClient
from pagemetadata_agent import PageMetaDataAgent

import datetime

class MongoDBAgent(PageMetaDataAgent):

    def __init__(self, config):
        c_copy =  dict(config)
        db = c_copy.pop('db')
        rawpages_collection = c_copy.pop('rawpages_collection')

        self.client = MongoClient(**c_copy)
        self.db = self.client[db]
        self.rawpages_collection = self.db[rawpages_collection]

    def getLastDownloadTime(self, url):
        doc = self.rawpages_collection.find_one(url)
        if not doc:
            return None
        last_timestamp = datetime.datetime.fromisoformat(doc["last"])

        return last_timestamp
