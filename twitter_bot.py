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
    api.update_status('test post')
    sleep(100)
    # while True:
    #     api.update_status('The time is now ' + strftime('%H:%M:%S', localtime()) + ' in Los Angeles')
    #     sleep(random.randrange(3, 8, 1) * 60 * 60) # tweets every 3-8 hours
