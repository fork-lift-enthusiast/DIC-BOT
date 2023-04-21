import requests
from bs4 import BeautifulSoup
import pandas as pd

with open('words_dictionary.json.txt', 'r') as f:
    words = f.read().split()


from collections import Counter
word_freq = Counter(words)
sorted_words = sorted(word_freq.items(), key=lambda x: x[1])



#get request
#parse html
#get definition
def get_def(word):
    url = f'https://www.dictionary.com/browse/{[word]}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try: 
        definition = soup.find(class_='one-click-content').get_text()
    except AttributeError:
        definition = ''
    return definition

import tweepy 
import time
from datetime import datetime, timedelta

consumer_key = 'L7NZvehIdhcVLHiBYsdxjWAZE'
consumer_secret = 'OLdo5xA8xLrvW8Ae2KDrQkZTSF3jeC9JH6Vjp9LJU4kvza3veC'
access_token = '1491298012642963457-KaQteUiNbFKNIypiZ3ZoCHGInXM4n7'
access_token_secret = 'Z1bqkN8oqG6BRiccyeXU4xw8SgAVRBNAMdpJgoalb2AFs'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def lmc():
    while True:
        for word, freq in sorted_words:
            if freq ==1:
                definition = get_def(word)
                tweet = f'{word}: {definition}'
                tweet_obj = {'text': tweet}
                try:
                    response = api.request('POST', 'statuses/update', {'status': tweet_obj})

                except tweepy.TwitterServerError as error:
                    print(f"Error sending tweet: {error}")
                time.sleep(10)
        now = datetime.now()
        next_tweet_time = datetime(now.year, now.month, now.day, 9, 0, 0) if now.hour < 9 else datetime(now.year, now.month, now.day, 21, 0, 0)
        time_to_wait = (next_tweet_time - now).total_seconds()
        time.sleep(time_to_wait)
lmc()    