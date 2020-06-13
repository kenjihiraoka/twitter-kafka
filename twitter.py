import tweepy as tw
from kafka import KafkaProducer

import twitter_env as env
from tweepy.streaming import StreamListener

# TWITTER API CONFIGURATIONS
consumer_key = env.api_key
consumer_secret = env.api_secret_key
access_token = env.access_token
access_secret = env.access_secret_token

# TWITTER API AUTH
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tw.API(auth)


# Twitter Stream Listener
class KafkaPushListener(StreamListener):
    def __init__(self):
        # localhost:9092 = Default Zookeeper Producer Host and Port Adresses
        self.producer = KafkaProducer(bootstrap_servers="localhost:9092",
                                      retry_backoff_ms=1000,
                                      retries=3,
                                      request_timeout_ms=30000)

    def on_data(self, data):
        # Producer produces data for consumer
        # Data comes from Twitter
        self.producer.send("covid", bytes(data, "ascii"))
        return True

    def on_error(self, status):
        print(status)
        return True


# Twitter Stream Config
twitter_stream = tw.Stream(auth, KafkaPushListener())

# Produce Data that has Game of Thrones hashtag (Tweets)
twitter_stream.filter(track=["#covid", "#COVID", "#covid-19", "#COVID-19", "#covid19", "#COVID19"])
