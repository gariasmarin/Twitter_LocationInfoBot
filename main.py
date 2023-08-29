import tweepy
import keys
import time


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


def post(client_: tweepy.Client, message: str):
    client_id = client_.get_me().data.id
    client_.create_tweet(text=message)
    #client_.create_tweet(text=str(client_id))
    response = client_.get_users_mentions(client_id)
    print('Tweeted successfully!')


def reply(client_: tweepy.Client, message: str):
    client_id = client_.get_me().data.id
    response = client_.get_users_mentions(client_id)
    client_.create_tweet(in_reply_to_tweet_id=client_id, text=message)
    #while True:
        #response = client_.get_users_mentions(client_id)

        #if response.data != None:
          #  for tweet in response.data:
           #     try:
          #          client_.create_tweet(in_reply_to_tweet_id=client_id, text=message)
           #     except:
            #        pass
        #time.sleep(5)


if __name__ == '__main__':
    client = client()
    post(client, 'testing78')
    #reply(client, 'this is a reply method test ')
# include some changes
