FROM python:3.7-stretch

RUN mkdir /downloader
WORKDIR /downloader

#COPY feedparser-5.2.1.tar.gz .
#COPY kafka-python-1.4.3.tar.gz .
#RUN pip install feedparser-5.2.1.tar.gz kafka-python-1.4.3.tar.gz
RUN pip install feedparser kafka-python pymongo

COPY urlsource urlsource
COPY pagemetadata_agent pagemetadata_agent
COPY scheduler scheduler
COPY downloader downloader
COPY backendinterface backendinterface

COPY rawpagedata rawpagedata

COPY simpledownloadertokafka.py .

ENV KAFKA_BOOTSTRAP_SERVER kafka:9092
ENV KAFKA_URLS_TOPIC urls
ENV KAFKA_URLS_GROUP_ID downloader
ENV KAFKA_RAWPAGES_TOPIC rawpages

ENV MONGODB_HOST mongo
ENV MONGODB_DB default
ENV MONGODB_RAWPAGES_COLLECTION rawpages
ENV MONGODB_USERNAME downloader
ENV MONGODB_PASSWORD downloader

ENV URLS_FILE urls.txt
ENV INITIALPAGE https://www.berlin.de/polizei/polizeimeldungen/index.php/rss
ENV INITIALPAGE_BACKOFFSECONDS 3600

ENV DOWNLOADER_MODE html
ENV DOWNLOADER_SLEEP_SECONDS 5
