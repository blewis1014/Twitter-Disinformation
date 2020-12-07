import json
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns
import pandas as pd
from pandas import DataFrame
from operator import itemgetter

domains = []
domainStats = []    # {DOMAIN:domain, NUM_TWEETS:numTweets, NUM_ACCOUNT:numAccounts}
accounts = []
timeRange = []  # [min,max]
totalTweets = 0

def process():
    global totalTweets
    with open("tweets.json",'r') as f:
        data = json.load(f)
    
    totalTweets = len(data)
    
    findTimeRange(data)
    getAllAccounts(data)
    buildDomainStats(data)
        
            

def drawBarChart():
    #fig = plt.figure()
    domains = []
    numOfTweets = []
    dataframes = []
    for domain in domainStats:
        dom = domain["DOMAIN"]
        tweetCount = int(domain["NUM_TWEETS"])

        domains.append(dom)
        numOfTweets.append(tweetCount)
        #domains.append({dom,tweetCount})

    d_dict = {'Domain':domains,'Tweet Count':numOfTweets}

    df = pd.DataFrame(d_dict)
        

    
    figure(num=None, figsize=(20,25), dpi=80, facecolor='w', edgecolor='r')
    sns.barplot(x="Tweet Count", y="Domain", data=df)

    plt.title("Number of Tweets per Domain")
    #plt.bar(domains,numOfTweets)
    #ax = fig.add_axes([0,0,1,1])
    #ax.bar(domains,numOfTweets)
    plt.show()

def drawBarChartAccounts():
    
    domains = []
    numOfAccounts = []
    dataframes = []
    for domain in domainStats:
        dom = domain["DOMAIN"]
        accountCount = int(domain["NUM_ACCOUNTS"])

        domains.append(dom)
        numOfAccounts.append(accountCount)
        

    d_dict = {'Domain':domains,'Account Count':numOfAccounts}

    df = pd.DataFrame(d_dict)
        

    
    figure(num=None, figsize=(20,25), dpi=80, facecolor='w', edgecolor='r')
    sns.barplot(x="Account Count", y="Domain", data=df)

    plt.title("Number of Accounts per Domain")
    plt.show()


def readInDomains():
    with open("D2_D3_Table.txt",'r') as f:
        next(f)
        for line in f:
            (key,value) = line.split()
            domains.append(value)

def findTimeRange(data):
    times = []
    for item in data:
        times.append(item["TIME"])

    timeRange.append(min(times))
    timeRange.append(max(times))

def getAllAccounts(data):
    for i in data:
        if(i["ACCOUNT"] not in accounts):
            accounts.append(i["ACCOUNT"])

def buildDomainStats(data):
    for domain in domains:
        numTweetsPerDomain = 0
        accountsPerDomain = []
        for item in data:
            if(item["DOMAIN"] == domain):
                numTweetsPerDomain+=1
                if(item["ACCOUNT"] not in accountsPerDomain):
                    accountsPerDomain.append(item['ACCOUNT'])

        domain_dict = {"DOMAIN":domain, "NUM_TWEETS":numTweetsPerDomain, "NUM_ACCOUNTS":len(accountsPerDomain)}
        domainStats.append(domain_dict)

def writeStats():
    for item in domainStats:
        print("Domain: "+item["DOMAIN"])
        print("Number of Tweets: "+str(item["NUM_TWEETS"]))
        print("Number of Accounts: "+str(item["NUM_ACCOUNTS"]))
        print("\n")
    print("Total Number of Tweets: "+str(totalTweets))
    print("Total Number of Accounts: "+str(len(accounts)))
    print("Time Range: {"+timeRange[0]+" --- "+timeRange[1]+"}")

def exportDomainStats():
    sortedDomainStats = sorted(domainStats,key=itemgetter('NUM_TWEETS'), reverse=True)
    with open("DomainStatsForProcessing.txt",'w') as f:
        for item in sortedDomainStats:
            f.write(str(item)+'\n')
            


if __name__=='__main__':
    readInDomains()
    process()
    #drawBarChart()
    drawBarChartAccounts()
    #writeStats()
    #exportDomainStats()