import tweepy #import the tweepy library to be able to use it
import json #import the json library
#import config # the config file is imported, which contains the Twitter API keys and tokens 


TOKEN_KEY = "1897029080085860352-XoLtfep9Q0j9ZQQ42XlnCzfD8KkU10"
TOKEN_SECRET = "7cbJZoZwibQCqqK1wWIyZsyXZPrdupS390HgHhdMUMTPW"
API_KEY = "m6AbVGeucUTKrsp9cCvxH23lK"
API_SECRET = "3mFi8wAO1VL9ia2O4CNRqQPyFNz809NT40ISfT6VLLPo1k2ovi"
#The OAuth handler is initialised to access the Twitter API, since it is necessary for developers to identify themselves. The access token are set for the initialised OAuth handler.
auth = tweepy.OAuthHandler(API_KEY, API_SECRET) 
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET) 

#to access the Twitter API, the tweepy method is used. The wait_on_rate_limit is set to true, so that Twitter's API rate limit is respected.
api = tweepy.API(auth, wait_on_rate_limit=True)  

#hashtag, that is being searched for is defined; alternatively the following can be used to filter out retweets query = '#vegan -filter:retweets'
query = '#Remoteworking' 

#cursor method of Tweepy is used by utilising the search method. The count is set to 100 (max.limit) and the tweet_mode is extended, so that Tweets are not truncated. Pages is a set of 15 tweets
cursor = tweepy.Cursor(api.search_tweets, q=query, lang="en", count=100, tweet_mode='extended').pages() 

# the for loop iterates through the pages and for each page the second for loop iterates through the items and saves them in a list
for page in cursor:
    tweets = []
    for item in page:
        tweets.append(item._json)

#tweets list is dumped into a new JSON file 
with open('remoteworking', 'w') as outfile:
    json.dump(tweets,outfile)
