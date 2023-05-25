import tweepy
import keys



#OAuth2.0 is weird

def client():
    client = tweepy.Client(
        bearer_token=keys.bearer_token,
        consumer_key=keys.api_key,
        consumer_secret=keys.api_secret,
        access_token=keys.access_token,
        access_token_secret=keys.access_token_secret
    )

    return client

def tweet(client: tweepy.Client, message: str):

    client.create_tweet(message)

    print('Tweeted successfully!')


if __name__ == '__main__':
    client = client()
    tweet(client, 'This was tweeted from Python')
#include some changes