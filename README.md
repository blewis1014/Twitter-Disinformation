# Homework 10 - Disinformation
**Due:** Tuesday, May 5, 2020 by 3:30pm

*10 points - all extra credit*

## Extra Credit Assignment 

### Disinformation

Data Sources:
* D1 - domains shared in tweets in the ICWSM 2017 paper, related to mass shootings
* D2 - URIs shared in tweets in the ICWSM 2018 paper, related to work of White Helmets in Syria
* D3 - websites publishing false Coronavirus information, gathered by https://www.newsguardtech.com/coronavirus-misinformation-tracking-center/

**Q1.** *(x points)* The D2 dataset contains some shortened URIs and proxies. Process each URI and follow redirects until it resolves or there is a 40x HTTP status. Record the final URI, HTTP status, and tweet frequency information (from the original data file) and save in a separate data file. 

**Q2.** *(x points)* For each of the final URIs from Q1, check its archival status using MemGator (see HW2). For each, record the total number of mementos and the number of mementos from each year from 2016-2020.

**Q3.** *(x points)* For each of the final URIs from Q1, extract the domain from the URI. Create a list of unique domains and include the number of times that domain appeared in the dataset and the sum of tweets the domain appeared in. Compare the domains present in D2 (from your processed dataset in Q3) and in D1.  Is there an overlap?  Compare with the domains from D3.  How much overlap is there between the three datasets?

**Q4.** *(x points)* For each domain in D1 and D3, check its archival status using MemGator (see HW2). For each, record the total number of mementos and the number of mementos from each year from 2016-2020.

In your report, discuss any interesting findings you discover and suggest questions or potential for future investigation.

### Revisiting TimeMaps from HW2

**Q5.** *(x points)* Re-download the 1000 TimeMaps from HW2, Q2.  Create a graph where the x-axis represents the 1000 TimeMaps.  If a TimeMap has "shrunk", it will have a negative value below the x-axis corresponding to the size difference between the two TimeMaps.  If it has stayed the same, it will have a "0" value.  If it has grown, the value will be positive and correspond to the increase in size between the two TimeMaps.

As always, upload all the TimeMap data.  If the HW2 github has the original TimeMaps, then you can just point to where they are in 
the report.


## Submission

Make sure that you have committed and pushed your local repo to GitHub before the deadline.  Include "@weiglemc Ready to grade" in your commit comment.
