import json
from collections import Counter
from nltk.corpus import stopwords
import re
import nltk
import itertools

tweets= []
tweet_bodies = []
tweets_no_stops = []
all_words = []
most_common = []
common = []
tweets_with_common_terms = 0

def process():
    global tweets, tweet_bodies, tweets_no_stops, all_words
    with open("tweets.json",'r') as f:
        data = json.load(f)
        for item in data:
            tweet_dict = {'ID':item["ID"],'TEXT':item["TEXT_BODY"]}
            tweets.append(tweet_dict)
            text_no_url = removeUrlsAndSpecialChars(item["TEXT_BODY"]).lower()
            text_split = text_no_url.split() 
            tweet_bodies.append(text_split)

    #nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

    for text in tweet_bodies:
        temp = []
        for word in text:
                if word not in stop_words:
                    temp.append(word)
        tweets_no_stops.append(temp)
    
    for text in tweets_no_stops:
        for word in text:
            all_words.append(word)

def removeUrlsAndSpecialChars(txt):
    return " ".join(re.sub(r"([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

def getMostCommonTerms():
    global most_common, common
    common_words = Counter(all_words)

    most_common = common_words.most_common(22)
    del most_common[0:2]

    for item in most_common:
        common.append(item[0])

def checkCommonTerms():
    global tweets_with_common_terms
    for text in tweet_bodies:
        for word in common:
            breaker = False
            if word in text:
                tweets_with_common_terms+=1
                breaker = True
            if breaker:
                break

def output():
    print("Top 20 most common terms out of "+str(len(tweets))+" Tweets")
    for word in most_common:
        print(word)
    print("\nNumber of Tweets featuring a common term: "+str(tweets_with_common_terms))

if __name__=='__main__':
    process()
    getMostCommonTerms()
    checkCommonTerms()
    output()