import tweepy
import keys

# bearer_token = keys.bearer_token
# consumer_key = keys.api_key
# consumer_secret = keys.api_secret
# access_token = keys.access_token
# access_token_secret = keys.access_token_secret
#
# # OAuth2.0 is weird
#
# client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)


def client():
    client_ = tweepy.Client(
        bearer_token=keys.bearer_token,
        consumer_key=keys.api_key,
        consumer_secret=keys.api_secret,
        access_token=keys.access_token,
        access_token_secret=keys.access_token_secret
    )

    return client_


def tweet(client_: tweepy.Client, message: str):
    client_.create_tweet(text=message)

    print('Tweeted successfully!')


if __name__ == '__main__':
    client = client()
    tweet(client, 'This was tweeted from Python')
# include some changes
