import tweepy
from tweepy import OAuthHandler
import config
from pymongo import MongoClient
import time


mongo_client = MongoClient('localhost', 27017)
db = mongo_client.tdt4215
smallest_id = "0"

def process_tweets(search):
	for tweet in search:
		print tweet.text.encode('utf-8') 
		print "\n"
		smallest_id = tweet.id_str
		db.tweets.update({"_id": tweet.id}, {"$set":{"text": tweet.text.encode('utf-8'), "candidate": "berniesanders"}}, upsert=True)
	return smallest_id
 
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_secret = config.access_secret
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Get 100 initial tweets
search = api.search(q='@berniesanders', count=100, lang="en", until="2016-04-06")


# Process tweets until we are blocked
for i in range(0, 449):
	try:
		search = api.search(q='@berniesanders', count=100, lang="en", max_id=process_tweets(search), until="2016-04-06")
	except:
		print "Sleeping..."
		time.sleep(5)
		pass
 
api = tweepy.API(auth)
search = api.search(q='#lol', count=100, lang="en", since_id="2016-04-05", until="2016-04-05", geocode="43.053998,-87.946676,130km")

for tweet in search:
	print tweet.text, '\n'
