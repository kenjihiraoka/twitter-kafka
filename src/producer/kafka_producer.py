import logging

from datetime import datetime
from kafka import KafkaProducer
from kafka.errors import KafkaError


class KafkaEventProducer:
    def __init__(self, bootstrap_servers):
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                      retry_backoff_ms=1000,
                                      retries=3,
                                      request_timeout_ms=30000)

    def send_massage(self, topic, message):
        response = self.producer.send(topic, message)

        try:
            metadata = response.get(timeout=10)
            logging.debug(
                f"{str(datetime.now())} - Event publish successfully! "
                f"TOPIC: {metadata.topic}, "
                f"PARTITION: {metadata.partition}, "
                f"OFFSET: {metadata.offset}"
            )
        except KafkaError as err:
            logging.error(f"Verify KAFKA_PRODUCER_BOOTSTRAP_SERVERS availability.\n {err}")
