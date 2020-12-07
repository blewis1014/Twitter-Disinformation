import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import requests
from requests.exceptions import ConnectionError
import csv
import json
from operator import itemgetter
from urllib.parse import urlparse
import socket
import ast

allURIs = []    #  {'OG_URI': og, 'FREQUENCY': count, 'FINAL_URI': final, 'STATUS': http}
uniqueDomains = []  #  {'DOMAIN': domain, 'NUM_IN_DATA':dataCount,'NUM_IN_TWEETS':tweetCount}
sortedDomains = []
diff_URI_Count = 0
status200 = 0
status404 = 0
count = 1



def process():
    #loop_count = 0
    with open("expanded-URLs.csv",'r') as f:
        for line in csv.DictReader(f):
            #if(loop_count==100):
                #break
            uri = line['Article URL']
            freq = line['total_freq']
            final_uri, status = processHTTPStatus(uri)
            all_dict = {'OG_URI': uri, 'FREQUENCY': freq, 'FINAL_URI': final_uri, 'STATUS': status}
            allURIs.append(all_dict)
            #loop_count+=1

    for item in allURIs:
        item_uri = item['FINAL_URI']
        item_freq = item['FREQUENCY']
        extractDomain(item_uri,item_freq)

    global sortedDomains
    sortedDomains = sorted(uniqueDomains,key=itemgetter('NUM_IN_DATA'), reverse=True)

    
def extractDomain(uri,frequency):
    domain = urlparse(uri).netloc
    domain_dict = {'DOMAIN':domain,'NUM_IN_DATA':1,'NUM_IN_TWEETS':frequency}
    exists = False
    exists_index = 0

    for index, dom in enumerate(uniqueDomains):
        if domain == dom['DOMAIN']: 
            exists = True
            exists_index = index
            

    if exists == False:    
        uniqueDomains.append(domain_dict)
    else:
        uniqueDomains[exists_index]['NUM_IN_DATA']+=1


def processHTTPStatus(uri):
    global status200, status404, diff_URI_Count, count
    final_url=""
    status=""
    print("Processing URI "+str(count)+": "+uri)
    try:
        response = requests.get(uri,timeout=20)
        final_url = response.url
        status = response.status_code
        if(final_url != uri):
            diff_URI_Count+=1
    except (ConnectionError, requests.exceptions.Timeout, requests.exceptions.ReadTimeout, requests.exceptions.TooManyRedirects):
        print("Connection Error")
        final_url = uri
        status = 0
    except socket.timeout:
        print("Timeout Error")
        final_url = uri
        status = 0

    if status == 200:
        status200+=1
    else:
        status404+=1

    print("Done")
    count+=1

    return(final_url, status)

def write_URIs_To_File():
    with open("ProcessedURIs.txt","w") as f:
        for item in allURIs:
            f.write(str(item)+"\n")

def write_Domain_To_File():
    with open("UniqueDomainsForProc.txt","w") as f:
        #f.write("Number of Unique Domains: "+str(len(sortedDomains))+"/"+str(len(allURIs))+"\n\n")   
        for item in sortedDomains:
            f.write(str(item)+"\n")
            #f.write("Domain: "+item['DOMAIN']+"\n")
            #f.write("Frequency in Data: "+str(item['NUM_IN_DATA'])+"\n")
            #f.write("Frequency in Twitter Posts: "+str(item['NUM_IN_TWEETS'])+"\n\n")
             


def outputURIs():
    global status200, status404, diff_URI_Count
    print("\n")
    for item in allURIs:
        print("URI:"+str(item["OG_URI"]))
        print("Frequency:"+str(item["FREQUENCY"]))
        print("Final URI:"+str(item["FINAL_URI"]))
        print("Status:"+str(item["STATUS"]))
        print("\n")
    
    print("\n")

def outputDomains():
    print("Unique Domains: \n")
    for item in uniqueDomains:
        print("Domain: "+item['DOMAIN'])
        print("Data Frequency: "+str(item['NUM_IN_DATA']))
        print("Tweet Frequency: "+str(item['NUM_IN_TWEETS']))
        print("\n")
    print("\n")
    
    
def outputStats():
    global status200, status404
    print("URIs with 200 response: "+str(status200))
    print("URIs with 404 response: "+str(status404))
    print("URIs redirected to different URIs: "+str(diff_URI_Count)+"\n")

    #print("Unique Domains: "+str(unique_domain_count))
    print("Unique Domains: "+str(len(uniqueDomains)))
    #print("Unique Domain List Size: "+ str(len(uniqueDomains)))
    
def readURIsForDomains():
    with open("ProcessedURIs.txt",'r') as f:
        for line in f:
            new_dict = ast.literal_eval(line)
            uri = new_dict['FINAL_URI']
            freq = new_dict['FREQUENCY']
            extractDomain(uri,freq)
    global sortedDomains
    sortedDomains = sorted(uniqueDomains,key=itemgetter('NUM_IN_DATA'), reverse=True)

if __name__=='__main__':
    process()
    #readURIsForDomains()
    #outputURIs()
    #outputDomains()
    write_URIs_To_File()
    write_Domain_To_File()
    outputStats()