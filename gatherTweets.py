import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import time
import traceback
import math

domains = []
tweets = []
domainStats = []    # {DOMAIN:domain, NUM_TWEETS:numTweets, NUM_ACCOUNT:numAccounts}
accounts = []

LIMIT = 200
totalTweetCount = 0
lowestTime = 0
highestTime = 0


# Keys ommitted 
consumer_key="***"
consumer_secret="***"
access_token="***"
access_secret="***"

# Handles authorization with Twitter
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#api = tweepy.API(auth)

def readInDomains():
    with open("D1_D3_Table.txt",'r') as f:
        next(f)
        for line in f:
            (key,value) = line.split()
            domains.append(value)
        

def getTweets():
    global totalTweetCount

    for domain in domains:
        print("Fetching: "+domain)
        activeTweetCount = 0    #Number of tweets per domain
        for tweet in tweepy.Cursor(api.search, q="url:"+ domain +" -filter:retweets", lang="en").items(LIMIT):
            print("Tweet "+str(activeTweetCount+1))

            for url in tweet.entities["urls"]:
                tweet_ID = tweet.id_str
                tweet_Account = tweet.user.screen_name
                tweet_Time = tweet.created_at.strftime("%Y%m%d%H%M%S")
                tweet_Link = tweet.entities["urls"][0]["expanded_url"]
                tweet_Text = tweet.text
            
                tweet_dict = {'ID':tweet_ID,'ACCOUNT':tweet_Account,'TIME':tweet_Time,'DOMAIN':domain,
                'LINK':tweet_Link,'TEXT_BODY':tweet_Text}

                tweets.append(tweet_dict)
                totalTweetCount+=1
            
            activeTweetCount+=1

        print("Domain Closed"+"\n")

def exportToJSON():
    with open("tweets.json",'w') as f:
        json.dump(tweets, f, indent=2)

def writeStats():
    pass

if __name__=='__main__':
    readInDomains()
    getTweets()
    exportToJSON()