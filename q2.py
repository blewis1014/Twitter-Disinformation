import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from operator import itemgetter
import ast
import csv
import re

d1 = []
d2 = [] #From Q1
d3 = []

domainsInD1_D2 = []
domainsInD2_D3 = []
domainsInD1_D3 = []

domainsInAll = []


def readD1():
    with open("D1.csv",'r') as f:
        for line in csv.DictReader(f):
            d1_dict = {'DOMAIN':line["Domain"]}
            d1.append(d1_dict)

def readD2():
    with open("UniqueDomainsForProc.txt",'r') as f:
        for line in f:
            d2_dict = ast.literal_eval(line)
            d2.append(d2_dict)

def readD3():
    with open("D3.csv",'r') as f:
        for line in csv.DictReader(f):
            d3_dict = {'DOMAIN':line["Domain"],'COUNTRY':line['Country']}
            d3.append(d3_dict)

def compareDomains():
    for d1Item in d1:
        dom1 = d1Item['DOMAIN']
        #print(dom1+'\n')
        for d2Item in d2:
            dom2 = d2Item['DOMAIN']
            if dom2.startswith('www.'):
                dom2 = re.sub(r'www.','',dom2)
            #print(dom2+'\n')
            if (dom1 == dom2):
                if dom2 not in domainsInD1_D2:
                    domainsInD1_D2.append(dom2)

            for d3Item in d3:
                dom3 = d3Item['DOMAIN']
                dom3 = dom3.lower()

                if (dom1 == dom3):
                    if dom3 not in domainsInD1_D3:
                        domainsInD1_D3.append(dom3)
                if (dom2 == dom3):
                    if dom3 not in domainsInD2_D3:
                        domainsInD2_D3.append(dom3)
                if (dom1 == dom2 and dom2 == dom3):
                    if dom3 not in domainsInAll:
                        domainsInAll.append(dom3)
    
    
def drawTable():
    sorted12 = sorted(domainsInD1_D2)
    sorted23 = sorted(domainsInD2_D3)
    sorted13 = sorted(domainsInD1_D3)
    sortedAll = sorted(domainsInAll)


    table1 = pd.DataFrame({
        'D1 & 2': sorted12,
    })

    table2 = pd.DataFrame({
        'D2 & 3': sorted23,
    })

    table3 = pd.DataFrame({
        'D1 & 3': sorted13,
    })

    table4 = pd.DataFrame({
       'In All': sortedAll,
    })

    print(table1)
    print("\n")
    print(table2)
    print("\n")
    print(table3)
    print("\n")
    print(table4)

if __name__=='__main__':
    readD1()
    readD2()
    readD3()
    compareDomains()
    drawTable()