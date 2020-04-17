# Homework 10 - Analyzing Disinformation Domains
**Due:** Tuesday, May 5, 2020 by 3:30pm

*10 points - all extra credit*

## Data Sources:
* [D1](https://docs.google.com/spreadsheets/d/1lk3pFSc5wo3OfJc8ekONqO3MJCCigqe8SBSYwLYlHLo/) - 117 domains shared in tweets in the ICWSM 2017 paper, related to mass shootings
* [D2]() - 1679 URIs shared in tweets in the ICWSM 2018 paper, related to work of White Helmets in Syria
  * *this dataset was sent to ODU for research purposes, so do not share*
* [D3](https://docs.google.com/spreadsheets/d/1VaSxEskGWPeGo5zHEjahVAYu2gKSzSLskLA3etJAuNU/) - 178 domains publishing false Coronavirus information, gathered by https://www.newsguardtech.com/coronavirus-misinformation-tracking-center/

*Google spreadsheets can be downloaded as CSV or TSV files using the File...Download... menu option*

## Assignment 

Write a report that answers and explains your answers to the following questions. Support your answers by including all relevant discussion, assumptions, examples, etc. You must describe how you answered the questions. Your GitHub repo should include all scripts, code, output files, images needed to complete the assignment. If you use a Google Colab notebook, you must save a copy in GitHub in your HW10 repo.

In your report, discuss any interesting findings you discover and suggest questions or potential for future investigation.

**Q1.** *(x points)* The D2 dataset contains some shortened URIs and proxies. Process each URI and follow redirects until it resolves or there is a 40x HTTP status. Record the final URI and current HTTP status.

For each of the final URIs, check its archival status using MemGator (see HW2). Record the date of the first memento, total number of mementos, and the number of mementos in each year from 2016-2020.  

Save a data file that contains the original URI, tweet frequency (from the original data file), final URI (many of these will be the same as the original URI), current HTTP status, date of first memento, total number of mementos, and number of mementos in each year from 2016-2020.

**Q2.** *(x points)*  For each of the final URIs from Q1, extract the domain from the URI. Create a list of unique domains and include the number of times that domain appeared in the dataset and the sum of tweets the domain appeared in. 

**Q3.** *(x points)* Compare the domains present in D2 (from your processed dataset in Q2) and in D1.  Is there an overlap?  Compare with the domains from D3.  How much overlap is there between the three datasets?  *Receiving all the points for this question requires thoughtful discussion of the results.*

**Q4.** *(x points)* For each domain in D1 and D3, check its archival status using MemGator (see HW2). For each, record the total number of mementos and the number of mementos from each year from 2016-2020.

Note that most of the domains in D3 should have at least 1 memento because the Internet Archive has created an Archive-It collection of these sites (see https://archive-it.org/collections/13559).

**Q5.** *(x points)* Create the following charts based on the collected data.

1. Scatterplot of URI vs. datetime of the first memento and last memento (x-axis), sorted by the datetime of the first memento.  Color dots based on the dataset it comes from. This should look similar to this [chart of URIs vs. memento datetimes](https://3.bp.blogspot.com/-8vNC-7UraiQ/U43lwAC0pSI/AAAAAAAAAE4/1IyHbXH9CKQ/s1600/mementosScatterDmoz.png), but with only the first and last dot on each row plotted (since you're only plotting the datetimes of the first and last mementos).

2. Histogram of mementos per year for 2016-2020 for D1. The year should be on the x-axis and the number of domains with any mementos that year should be on the y-axis.

*Need to talk about graphs to generate.  Histogram of domains that have mementos in 2016-2020, URI vs. date of first memento*

## Submission

Make sure that you have committed and pushed your local repo to GitHub before the deadline.  Include "@weiglemc Ready to grade" in your commit comment.
