from kafka import KafkaConsumer
from urlsource import URLSource

class KafkaSource(URLSource):

    def __init__(self, config):
        config["key_deserializer"] = lambda k: k.decode('utf-8')
        config["value_deserializer"] = lambda v: v.decode('utf-8')
        topic = config.pop("topic")
        self.consumer = KafkaConsumer(topic, **config)

    def getURL(self):
        msg = next(self.consumer)
        assert isinstance(msg.value, str)
        return msg.value
