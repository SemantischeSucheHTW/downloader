from urlsource import KafkaSource
from pagemetadata_agent import MongoDBAgent
from scheduler import ImprovedScheduler
from downloader import ImprovedDownloader
from backendinterface import KafkaBackendInterface

import os

env = lambda key: os.environ.get(key)

urlSource = KafkaSource({
        'bootstrap_servers': env('KAFKA_BOOTSTRAP_SERVER'),
        'topic': env('KAFKA_URLS_TOPIC'),
        'group_id': env("KAFKA_URLS_GROUP_ID")
})

pagemetadata_agent = MongoDBAgent({
        "host": env("MONGODB_HOST"),
        "db": env("MONGODB_DB"),
        "rawpages_collection": env("MONGODB_RAWPAGES_COLLECTION"),
        "username": env("MONGODB_USERNAME"),
        "password": env("MONGODB_PASSWORD"),
        "authSource": env("MONGODB_DB")
})

scheduler = ImprovedScheduler(
        env('URLS_FILE'),
        pagemetadata_agent,
        env('INITIALPAGE'),
        int(env('INITIALPAGE_BACKOFFSECONDS'))
)

backendinterface = KafkaBackendInterface({
        'bootstrap_servers': env('KAFKA_BOOTSTRAP_SERVER'),
        'topic': env('KAFKA_RAWPAGES_TOPIC')
})

downloader = ImprovedDownloader(
        scheduler,
        backendinterface,
        env('DOWNLOADER_MODE'),
        int(env('DOWNLOADER_SLEEP_SECONDS')),
)

downloader.run()

while True:
    scheduler.putURL(urlSource.getURL())
