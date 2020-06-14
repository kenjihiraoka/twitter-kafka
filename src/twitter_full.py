import sys
import json
import requests

from pprint import pprint
from authentication import Authentication

sys.path.append(".")
import twitter_env as env

STREAM_URL = "https://api.twitter.com/labs/1/tweets/stream/sample"


class TwitterFull:
    @staticmethod
    def stream_connect(authentication):
        with requests.get(STREAM_URL, auth=authentication,
                          headers={"User-Agent": "TwitterDevSampledStreamQuickStartPython"},
                          stream=True) as response:
            for response_line in response.iter_lines(chunk_size=20):
                if response_line:
                    pprint(json.loads(response_line))


if __name__ == "__main__":
    stream = TwitterFull()
    auth = Authentication(twitter_consumer_key=env.api_key,
                          twitter_consumer_secret=env.api_secret_key)

    while True:
        stream.stream_connect(authentication=auth)
