import tweepy
import random
from keys import keys
from time import localtime, strftime, sleep
 
CONSUMER_KEY = keys['consumer_key'] 
CONSUMER_SECRET = keys['consumer_secret'] 
ACCESS_KEY = keys['access_token']
ACCESS_SECRET = keys['access_token_secret']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

if __name__ == '__main__':
    for status in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(status.id)
            print("Deleted:", status.id)
        except:
            print("Failed to delete:", status.id)
