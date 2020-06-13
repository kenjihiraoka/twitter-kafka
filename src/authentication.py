import requests

from requests.auth import AuthBase


class Authentication(AuthBase):
    def __init__(self, twitter_consumer_key, twitter_consumer_secret):
        self.bearer_token_url = "https://api.twitter.com/oauth2/token"
        self.consumer_key = twitter_consumer_key
        self.consumer_secret = twitter_consumer_secret
        self.bearer_token = self.get_bearer_token()

    def get_bearer_token(self):
        response = requests.post(
            self.bearer_token_url,
            auth=(self.consumer_key, self.consumer_secret),
            data={'grant_type': 'client_credentials'},
            headers={"User-Agent": "TwitterDevSampledStreamQuickStartPython"})

        if response.status_code is not 200:
            raise Exception(f"Cannot get a Bearer token (HTTP {response.status_code}): {response.text}")

        body = response.json()
        return body['access_token']

    def __call__(self, r):
        r.headers['Authorization'] = f"Bearer {self.bearer_token}"
        return r
