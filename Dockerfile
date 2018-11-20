FROM python:3.7-stretch

RUN mkdir /downloader
WORKDIR /downloader

#COPY feedparser-5.2.1.tar.gz .
#COPY kafka-python-1.4.3.tar.gz .
#RUN pip install feedparser-5.2.1.tar.gz kafka-python-1.4.3.tar.gz
RUN pip install feedparser kafka-python

COPY backend_interface.py .
COPY downloader.py .
COPY mvp.py . 
COPY raw_page.py .

ENV KAFKA_BOOTSTRAP_SERVER kafka:9092
ENV KAFKA_RAWPAGE_TOPIC rawpages
