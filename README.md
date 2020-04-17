# Homework 10 - Disinformation
**Due:** Tuesday, May 5, 2020 by 3:30pm

*10 points - all extra credit*

## Extra Credit Assignment 

### Disinformation

Data Sources:
* D1 - 117 domains shared in tweets in the ICWSM 2017 paper, related to mass shootings
  * available at https://docs.google.com/spreadsheets/d/1lk3pFSc5wo3OfJc8ekONqO3MJCCigqe8SBSYwLYlHLo/edit#gid=0
* D2 - 1679 URIs shared in tweets in the ICWSM 2018 paper, related to work of White Helmets in Syria
  * available at  (*do not share this dataset outside of this class, was sent to ODU for research purposes*)
* D3 - websites publishing false Coronavirus information
  * available at https://www.newsguardtech.com/coronavirus-misinformation-tracking-center/
  * this will need to be turned into a csv or text file listing the domains -- note that the links lead to information about the domains rather than the domains themselves, so if scraping, only grab the anchor text, not the `href`
    * *1 point extra extra credit* - first person to create the file, upload to a public GitHub repo, and post a link in Piazza with the tag "hw10" - it doesn't matter if you write a program to scrape the webpage or just copy/paste, but the resulting file should be easily usable by everyone

**Q1.** *(x points)* The D2 dataset contains some shortened URIs and proxies. Process each URI and follow redirects until it resolves or there is a 40x HTTP status. Record the final URI, HTTP status, and tweet frequency information (from the original data file) and save in a separate data file. 

**Q2.** *(x points)* For each of the final URIs from Q1, check its archival status using MemGator (see HW2). Record the date of the first memento, total number of mementos, and the number of mementos in each year from 2016-2020.  Add this information to the data file from Q1.

**Q3.** *(x points)* For each of the final URIs from Q1, extract the domain from the URI. Create a list of unique domains and include the number of times that domain appeared in the dataset and the sum of tweets the domain appeared in. Compare the domains present in D2 (from your processed dataset in Q3) and in D1.  Is there an overlap?  Compare with the domains from D3.  How much overlap is there between the three datasets?

**Q4.** *(x points)* For each domain in D1 and D3, check its archival status using MemGator (see HW2). For each, record the total number of mementos and the number of mementos from each year from 2016-2020.

Note that most of the domains in D3 should have at least 1 memento because the Internet Archive has created an Archive-It collection of these sites (see https://archive-it.org/collections/13559).

*Need to talk about graphs to generate.  Histogram of domains that have mementos in 2016-2020, URI vs. date of first memento*

In your report, discuss any interesting findings you discover and suggest questions or potential for future investigation.

### Revisiting TimeMaps from HW2

**Q5.** *(x points)* Re-download the 1000 TimeMaps from HW2, Q2.  Create a graph where the x-axis represents the 1000 TimeMaps.  If a TimeMap has "shrunk", it will have a negative value below the x-axis corresponding to the size difference between the two TimeMaps.  If it has stayed the same, it will have a "0" value.  If it has grown, the value will be positive and correspond to the increase in size between the two TimeMaps.

As always, upload all the TimeMap data.  If the HW2 github has the original TimeMaps, then you can just point to where they are in 
the report.


## Submission

Make sure that you have committed and pushed your local repo to GitHub before the deadline.  Include "@weiglemc Ready to grade" in your commit comment.
