from kafka import KafkaProducer
import json

class KafkaBackend:
    def __init__(self, config, topic):
        config["key_serializer"] = str.encode
        config["value_serializer"] = lambda v: json.dumps(v).encode('utf-8')
        self.producer = KafkaProducer(**config)
        self.topic = topic

    def sendOff(self, rawPageData):
        key = rawPageData.url
        value = {
                'url': rawPageData.url,
                'datetime': rawPageData.datetime.isoformat(),
                'protocol': rawPageData.protocol,
                'statuscode': rawPageData.statuscode,
                'header': rawPageData.header,
                'body': rawPageData.body,
        }
        self.producer.send(self.topic, key=key, value=value)
