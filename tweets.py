import tweepy
from tweepy import OAuthHandler
import config
 
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_secret = config.access_secret
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
search = api.search(q='#lol', count=100, lang="en", since_id="2016-04-05", until="2016-04-05", geocode="43.053998,-87.946676,130km")

for tweet in search:
	print tweet.text, '\n'