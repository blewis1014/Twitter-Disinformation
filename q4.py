import json
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns
import pandas as pd
from pandas import DataFrame
import ast
import csv
from operator import itemgetter
import re

d1 = [] # DOMAIN, NUM_CITATIONS
d2 = [] # DOMAIN, NUM_IN_TWEETS
q3 = [] # DOMAIN, NUM_TWEETS

domainsInD1_Q3 = [] # DOMAIN, TOTAL_FREQ, D1_FREQ, Q1_FREQ
domainsInD2_Q3 = [] # DOMAIN, D2_FREQ, Q1_FREQ


def readD2():
    global d2
    temp = []
    with open("UniqueDomainsForProc.txt",'r') as f:
        for line in f:
            d2_dict = ast.literal_eval(line)
            temp.append(d2_dict)
    for item in temp:
        if item["NUM_IN_TWEETS"] == "":
            item["NUM_IN_TWEETS"] = 0
        else:
            item["NUM_IN_TWEETS"] = int(item["NUM_IN_TWEETS"])

    d2 = sorted(temp,key=itemgetter("NUM_IN_TWEETS"), reverse=True)

def readD1():
    global d1
    temp = []
    with open("D1.csv",'r') as f:
        for line in csv.DictReader(f):
            if line["# Citations in our Alternative Narrative Tweets"] == "":
                d1_dict = {'DOMAIN':line["Domain"], 'NUM_CITATIONS':0}
            else:
                d1_dict = {'DOMAIN':line["Domain"], 'NUM_CITATIONS':int(line["# Citations in our Alternative Narrative Tweets"])}
            temp.append(d1_dict)

    d1 = sorted(temp,key=itemgetter("NUM_CITATIONS"), reverse=True)

def readQ3():
    with open("DomainStatsForProc.txt",'r') as f:
        for line in f:
            q3_dict = ast.literal_eval(line)
            q3.append(q3_dict)

def compareDomains():
    global domainsInD1_Q3, domainsInD2_Q3
    temp1 = []
    for d1Item in d1:
        dom1 = d1Item['DOMAIN']

        for q3Item in q3:
            dom3 = q3Item['DOMAIN']

            if (dom1 == dom3):
                if dom3 not in domainsInD1_Q3:
                    d1_freq = d1Item["NUM_CITATIONS"]
                    q3_freq = q3Item["NUM_TWEETS"]
                    tot_freq = d1_freq + q3_freq
                    new_dict = {"DOMAIN":dom3,"TOTAL_FREQ":tot_freq,"D1_FREQ":d1_freq,"Q3_FREQ":q3_freq}
                    temp1.append(new_dict)

    domainsInD1_Q3 = sorted(temp1, key = itemgetter("TOTAL_FREQ"), reverse=True)

    temp2 = []
    for d2Item in d2:
        dom2 = d2Item['DOMAIN']
        if dom2.startswith('www.'):
            dom2 = re.sub(r'www.','',dom2)

        for q3Item in q3:
            dom3 = q3Item['DOMAIN']

            if (dom2 == dom3):
                if dom3 not in domainsInD2_Q3:
                    d2_freq = d2Item["NUM_IN_TWEETS"]
                    q3_freq = q3Item["NUM_TWEETS"]
                    tot_freq = d2_freq + q3_freq
                    new_dict = {"DOMAIN":dom3,"TOTAL_FREQ":tot_freq,"D2_FREQ":d2_freq,"Q3_FREQ":q3_freq}
                    temp2.append(new_dict)
                      
    domainsInD2_Q3 = sorted(temp2, key = itemgetter("TOTAL_FREQ"), reverse=True)

def output(list):
    for item in list:
        print(item)

    print("\nNum in list: "+str(len(list)))

def exportComparisonStats():
    with open("Q4Stats.txt","w") as f:
        print("Top 5 Shared Domains in Set D1_Q3:"+"\n")
        f.write("Top 5 Shared Domains in Set D1_Q3:"+"\n\n")
        breaker = 0
        for item in domainsInD1_Q3:
            if breaker == 5:
                break
            domain = item["DOMAIN"]
            tot_freq = item["TOTAL_FREQ"]
            d1_freq = item["D1_FREQ"]
            q3_freq = item["Q3_FREQ"]
            print(
                "Domain: "+domain+"\n"
                "Total Tweet Count from Domain in Set: "+str(tot_freq)+"\n"
                "Tweet Count from D1: "+str(d1_freq)+"\n"
                "Tweet Count from Q3: "+str(q3_freq)+"\n"
            )
            f.write(
                "Domain: "+domain+"\n"
                "Total Tweet Count from Domain in Set: "+str(tot_freq)+"\n"
                "Tweet Count from D1: "+str(d1_freq)+"\n"
                "Tweet Count from Q3: "+str(q3_freq)+"\n\n" 
            )
            breaker+=1

        #print("\n")
        #for x in range(20):
        print("--"*20)
        f.write("--"*20)

        print("\n")
        f.write("\n\n")

        print("Top 5 Shared Domains in Set D1_Q3:"+"\n")
        f.write("Top 5 Shared Domains in Set D1_Q3:"+"\n\n")
        breaker = 0
        for item in domainsInD2_Q3:
            if breaker == 5:
                break
            domain = item["DOMAIN"]
            tot_freq = item["TOTAL_FREQ"]
            d2_freq = item["D2_FREQ"]
            q3_freq = item["Q3_FREQ"]
            print(
                "Domain: "+domain+"\n"
                "Total Tweet Count from Domain in Set: "+str(tot_freq)+"\n"
                "Tweet Count from D2: "+str(d2_freq)+"\n"
                "Tweet Count from Q3: "+str(q3_freq)+"\n"
            )
            f.write(
                "Domain: "+domain+"\n"
                "Total Tweet Count from Domain in Set: "+str(tot_freq)+"\n"
                "Tweet Count from D2: "+str(d2_freq)+"\n"
                "Tweet Count from Q3: "+str(q3_freq)+"\n\n" 
            )
            breaker+=1

def drawD1Q3Graph():
    dataset = []
    domain =[]
    frequency = []
    count=0
    for item in domainsInD1_Q3:
        if count == 5:
            break
        dom = item["DOMAIN"]
        d1 = item["D1_FREQ"]
        q3 = item["Q3_FREQ"]

        dataset.append("D1")
        domain.append(dom)
        frequency.append(d1)

        dataset.append("Q3")
        domain.append(dom)
        frequency.append(q3)

        count+=1
      
    data_dict = {"Dataset":dataset,"Domain":domain,"Frequency":frequency}
    df = pd.DataFrame(data_dict)

    pal = {"Q3": "darkviolet", "D1": "orangered"}

    sns.catplot(y="Domain", x="Frequency", hue="Dataset", palette=pal, kind ="bar",data=df, height=5, aspect=1.5)

    plt.ylabel("Domain")
    plt.xlabel("Tweet Count")
    plt.title("Number of Tweets per Domain")
    plt.show()

def drawD2Q3Graph():
    dataset = []
    domain =[]
    frequency = []
    count=0
    for item in domainsInD2_Q3:
        if count == 5:
            break
        dom = item["DOMAIN"]
        d2 = item["D2_FREQ"]
        q3 = item["Q3_FREQ"]

        dataset.append("D2")
        domain.append(dom)
        frequency.append(d2)

        dataset.append("Q3")
        domain.append(dom)
        frequency.append(q3)

        count+=1
      
    data_dict = {"Dataset":dataset,"Domain":domain,"Frequency":frequency}
    df = pd.DataFrame(data_dict)

    pal = {"Q3": "darkviolet", "D2": "gold"}

    sns.catplot(y="Domain", x="Frequency", hue="Dataset", palette=pal, kind ="bar",data=df, height=5, aspect=1.5)

    plt.ylabel("Domain")
    plt.xlabel("Tweet Count")
    plt.title("Number of Tweets per Domain")
    plt.show()
    

if __name__=='__main__':
    readD1()
    readD2()
    readQ3()
    compareDomains()
    #output(domainsInD1_Q3)
    #drawD1Q3Graph()
    #drawD2Q3Graph()
    exportComparisonStats()