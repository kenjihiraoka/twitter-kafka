from kafka.errors import KafkaError
from kafka import KafkaProducer

from datetime import datetime
import logging


class KafkaProducer:
    def __init__(self, bootstrap_servers):
        """
        Initialize KafkaProducer subscriber
        :param bootstrap_servers: Bootstrap Server with port
        """
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                      retry_backoff_ms=1000,
                                      retries=3,
                                      request_timeout_ms=30000)

    def post_message(self, topic, message):
        """
        Post message in Kafka Topic
        :param topic: topic to publish messages
        :param message: message to be published
        :return:
        """
        response = self.producer.send(topic, message)
        try:
            metadata = response.get(timeout=10)
            logging.debug(
                f"{str(datetime.now())} - Event publish successfully! "
                f"TOPIC: {metadata.topic}, PARTITION: {metadata.partition}, OFFSET: {metadata.offset}"
            )
        except KafkaError as err:
            logging.error(f"Verify KAFKA_PRODUCER_BOOTSTRAP_SERVERS availability.\n {err}")
