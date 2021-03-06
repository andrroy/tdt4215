import tweepy
from tweepy import OAuthHandler
import config
from pymongo import MongoClient
import time
import sys


mongo_client = MongoClient('localhost', 27017)
db = mongo_client.tdt4215
smallest_id = "0"

def process_tweets(search):
	for tweet in search:
		print tweet.text.encode('utf-8') + str(tweet.created_at)
		print "\n"
		smallest_id = tweet.id_str
		db.tweets.update({"_id": tweet.id}, {"$set":{"text": tweet.text.encode('utf-8'), "candidate": "johnkasich"}}, upsert=True)
	return smallest_id
 
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_secret = config.access_secret
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Get 100 initial tweets
search = api.search(q='@johnkasich', count=100, lang="en", until="2016-04-06")


# Process tweets until we are blocked
for i in range(0, 449):
	try:
		search = api.search(q='@johnkasich', count=100, lang="en", max_id=process_tweets(search), until="2016-04-06")
	except:
		print sys.exc_info()[0]
		print "Sleeping..."
		time.sleep(5)
		pass