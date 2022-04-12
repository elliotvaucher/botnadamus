import tweepy
import requests
import json
from config import create_api
from os import environ
from time import sleep
import redis

api = create_api()

r = redis.from_url(os.environ.get("REDIS_URL"))

parameters = {
    'api_key': environ["GIPHY_KEY"]
    }

last_tweet_id = {}

""" def read_last_seen(FILE_NAME): 
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id): 
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return """

def read_last_seen(): 
    last_seen_id = last_tweet_id.get('tweet_id')
    return last_seen_id

def store_last_seen(last_seen_id):
    last_tweet_id['tweet_id'] = last_seen_id
    return  

def get_gif(): 
    response = requests.get("http://api.giphy.com/v1/gifs/random", params=parameters)
    random_gif = json.loads(response.text)
    global gif_url
    gif_url = random_gif['data']['bitly_url']
    
    return(gif_url)    

def main():
    tweets = api.mentions_timeline(since_id=read_last_seen(), tweet_mode="extended")
    
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