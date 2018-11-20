from backendinterface import BackendInterface
from kafka import KafkaProducer
import json

class KafkaBackendInterface(BackendInterface):
    def __init__(self, config, topic):
        config["key_serializer"] = str.encode
        config["value_serializer"] = lambda v: json.dumps(v).encode('utf-8')
        self.producer = KafkaProducer(**config)
        self.topic = topic

    def send(self, rawPageData):
        key = rawPageData.url
        value = {
                'url': rawPageData.url,
                'datetime': rawPageData.datetime.isoformat(),
                'statuscode': rawPageData.statuscode,
                'header': rawPageData.header,
                'body': rawPageData.body,
        }
        future = self.producer.send(self.topic, key=key, value=value)
        future.get(timeout=10)
