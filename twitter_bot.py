import tweepy
from os import listdir, environ
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import date, timedelta

 
CONSUMER_KEY = environ.get('consumer_key')
CONSUMER_SECRET = environ.get('consumer_secret') 
ACCESS_KEY = environ.get('access_token')
ACCESS_SECRET = environ.get('access_token_secret')
AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_KEY, ACCESS_SECRET)
API = tweepy.API(AUTH)
sched = BlockingScheduler()


def post_status(photo):
    API.update_with_media(f'./photos/{photo}')


date = date(2019, 1, 28)
photos = listdir('./photos')
interval = timedelta(days=1)
for photo in photos: 
    sched.add_job(post_status, 'date', run_date=date, args=[photo])
    date += interval

sched.start()