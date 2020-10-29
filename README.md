# Homework 6 - Analyzing Disinformation Domains
**Due:** Sunday, November 15, 2020 by 11:59pm

## Data Sources:
* [D1](https://docs.google.com/spreadsheets/d/1lk3pFSc5wo3OfJc8ekONqO3MJCCigqe8SBSYwLYlHLo/) - 117 domains shared in tweets in the ICWSM 2017 paper, related to mass shootings
* [D2](expanded%20URLs.csv) - 1679 URIs shared in tweets in the ICWSM 2018 paper, related to work of White Helmets in Syria
  * *this dataset was sent to ODU for research purposes, so do not share*
* [D3](https://docs.google.com/spreadsheets/d/1bjuMnAnDsiVWrIuGIIpsXKBqkYNrOehmx0_ZWGVI6d0/) - 347 domains publishing false Coronavirus information, gathered by https://www.newsguardtech.com/coronavirus-misinformation-tracking-center/ as of October 28, 2020

*Google spreadsheets can be downloaded as CSV or TSV files using the File...Download... menu option* 

## Assignment 

Write a report that answers the following questions. Support your answers by including all relevant discussion, assumptions, examples, etc. You must describe how you answered the questions and any interesting insights from your work. Your GitHub repo should include all scripts, code, output files, images needed to complete the assignment. If you use a Google Colab notebook, you must save a copy in GitHub in your HW6 repo.

### Q1

*(1 point)* The D2 dataset contains some shortened URIs and proxies. Process each URI and follow redirects until it resolves as a 200 or there is a 40x HTTP status. 

Save a data file that contains the original URI, tweet frequency (from the original data file), final URI (many of these will be the same as the original URI), and current HTTP status.

How many URIs redirected to a different URI?

How many of the final URIs reported a 200 OK?

How many of the final URIs reported a 404 Not Found (or some other non-200 status)?

### Q2

*(1 point)*  For each of the final URIs from Q1, extract the domain from the URI. For example, given the URI `https://en.wikipedia.org/wiki/Domain_name`, the domain is `wikipedia.org`, and for the URI `https://www.theregister.co.uk/2020/04/16/cloudflare_cobol/`, the domain is `theregister.co.uk`.

How many unique domains are there?

Save a data file that contains each unique domain, the number of times that domain appeared in the dataset, and the total number of tweets the domain appeared in. 

*Could combine Q1 and Q2*

*Should check domains in D1 and D3 for liveness*

*Could do some analysis of how many tweets the domains appeared in*

### Q3

*(2 points)* Compare the domains present in your processed D2 dataset (from Q2) and in D1.  Is there an overlap?  Compare with the domains from D3.  How much overlap is there between the three datasets?  

### Q4
*(3 points)*

Search for tweets sharing links from any live domain that shows up in 2 of the 3 datasets.  `q="url:stackoverflow.com"`

*Or search for tweets that contain "election" and then analyze tweets from there that contained links to any of these domains*

### Q5
*(3 points)*

Create a network graph, similar to Dr. Starbird's, where a domain shared in a tweet is a node and a link exists between two nodes if a single Twitter account shared both domains.  

For example, if @weiglemc shared a tweet with a link to www.odu.edu and another tweet with a link to www.lsu.edu, then there should be a link between node odu.edu and node lsu.edu.

Extra credit: Map the size of the node to the number of tweets the domain was shared in.




## Submission

Make sure that you have committed and pushed your local repo to GitHub. Your repo should contain any code you developed to answer the questions. Include "Ready to grade @weiglemc @brutushammerfist" in your final commit message.

Submit the URL of your report in Blackboard:
* Click on HW6 under Assignments in Blackboard
* Under "Assignment Submission", click the "Write Submission" button.
* Copy/paste the URL of your report into the edit box
  * should be something like https<nolink>://github.com/cs432-websci-fall20/hw6-disinfo-*username*/blob/master/HW6-report.{pdf,md}
* Make sure to "Submit" your assignment.
