import tweepy
import requests
import json
from config import create_api
import os
from os import environ
from time import sleep
import redis

# creating api object from config.py
api = create_api()

# creating redis object to SET 
# and GET tweet_id
r = redis.from_url(os.environ.get("REDIS_URL"))

# passing the GIPHY_KEY value to 
# access Giphy API
parameters = {
    'api_key': environ["GIPHY_KEY"]
    }

# setting the initial last tweet_id 
# at program initialization
r.set("tweet_id", 1552419431783010305)

# function that reads tweet_id from 
# redis server
def read_last_seen(): 
    last_seen_id = r.get('tweet_id')
    return last_seen_id

# function that stores the last_seen_id 
# to redis server
def store_last_seen(last_seen_id):
    r.set('tweet_id', last_seen_id)
    return  

# function that calls the giphy random endpoint
# and returns a gif_url
def get_gif(): 
    response = requests.get("http://api.giphy.com/v1/gifs/random", params=parameters)
    random_gif = json.loads(response.text)
    global gif_url
    gif_url = random_gif['data']['bitly_url']
    
    return(gif_url)    

# main function that calls the Twitter API, 
# looks for new tweets mentioning the bot, 
# and prints back a response with gif url.
def main():
    tweets = api.mentions_timeline(since_id=read_last_seen(), count=1, tweet_mode="extended")
    
    for tweet in reversed(tweets): 
        if tweet.user.screen_name != "botnadamus":
            print(str(tweet.id) + ' - ' + tweet.full_text)
            get_gif()
            api.update_status('@' + tweet.user.screen_name + ' ' + gif_url, tweet.id)
            store_last_seen(tweet.id)
    

if __name__ == "__main__":
    while True:
        main()
        sleep(15)
