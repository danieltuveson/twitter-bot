import tweepy
import random
from keys import keys
from time import localtime, strftime, sleep
from os import listdir
 
CONSUMER_KEY = keys['consumer_key'] 
CONSUMER_SECRET = keys['consumer_secret'] 
ACCESS_KEY = keys['access_token']
ACCESS_SECRET = keys['access_token_secret']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

if __name__ == '__main__':
    photos = listdir('./photos')
    for photo in photos:
        api.update_with_media(f'./photos/{photo}')
        sleep(60 * 60 * 24) # Sleeps for one day
    api.update_status('Welp I\'m out of photos. Hopefully I\'ll have some more soon')
