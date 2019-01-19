import tweepy
from keys import keys
from os import listdir
 
CONSUMER_KEY = keys['consumer_key'] 
CONSUMER_SECRET = keys['consumer_secret'] 
ACCESS_KEY = keys['access_token']
ACCESS_SECRET = keys['access_token_secret']
AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_KEY, ACCESS_SECRET)
API = tweepy.API(AUTH)

if __name__ == '__main__':
    photos = listdir('./photos')
    for photo in photos:
        API.update_with_media(f'./photos/{photo}')
        sleep(60 * 60 * 24) # Sleeps for one day
    API.update_status('Welp I\'m out of photos. Hopefully I\'ll have some more soon')
