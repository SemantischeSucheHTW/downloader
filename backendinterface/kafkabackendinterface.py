from backendinterface.backendinterface import BackendInterface
from kafka import KafkaProducer

import json

class KafkaBackendInterface(BackendInterface):
    def __init__(self, config):
        config["key_serializer"] = str.encode
        config["value_serializer"] = lambda v: json.dumps(v).encode('utf-8')

        c_copy = dict(config)
        topic = c_copy.pop("topic")
        self.producer = KafkaProducer(**c_copy)
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
