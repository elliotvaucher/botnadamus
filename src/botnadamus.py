import tweepy
import requests
import json
from config import create_api

api = create_api()

parameters = {
    'api_key': "GIPHY_KEY"
}

FILE_NAME = "last.txt"

def read_last_seen(FILE_NAME): 
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id): 
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode="extended")

def get_gif(): 
    response = requests.get("http://api.giphy.com/v1/gifs/random", params=parameters)
    random_gif = json.loads(response.text)
    global gif_url
    gif_url = random_gif["data"]["bitly_url"]
    
    return(gif_url)

for tweet in reversed(tweets): 
    if tweet.user.screen_name != "botnadamus":
        print(str(tweet.id) + ' - ' + tweet.full_text)
        get_gif()
        api.update_status('@' + tweet.user.screen_name + ' ' + gif_url, tweet.id)
        store_last_seen(FILE_NAME, tweet.id)
