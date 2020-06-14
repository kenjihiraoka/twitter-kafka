import sys
import requests

from authentication import Authentication
from producer.kafka_producer import KafkaEventProducer

sys.path.append(".")
import twitter_env as env

STREAM_URL = "https://api.twitter.com/labs/1/tweets/stream/sample"


class TwitterFull:
    def __init__(self):
        self.producer = KafkaEventProducer(bootstrap_servers=["localhost:9092"])

    def stream_connect(self, authentication):
        with requests.get(STREAM_URL, auth=authentication,
                          headers={"User-Agent": "TwitterDevSampledStreamQuickStartPython"},
                          stream=True) as response:
            for response_line in response.iter_lines(chunk_size=20):
                if response_line:
                    self.producer.send_massage("general-tweets", response_line)


if __name__ == "__main__":
    stream = TwitterFull()
    auth = Authentication(twitter_consumer_key=env.api_key,
                          twitter_consumer_secret=env.api_secret_key)

    while True:
        stream.stream_connect(authentication=auth)
