import downloader
from backend_interface import KafkaBackend
import os

kafkaConfig = {
        'bootstrap_servers': os.environ.get('KAFKA_BOOTSTRAP_SERVER')
}

print(kafkaConfig)

kafkaBackend = KafkaBackend(kafkaConfig, os.environ.get('KAFKA_RAWPAGE_TOPIC'))

print(os.environ.get('KAFKA_RAWPAGE_TOPIC'))

future = kafkaBackend.sendOff(downloader.download_html('https://www.google.de'))
print(future.get(timeout=10))
