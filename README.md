I worked with my peers Kiet Hoang, Mike Pointek, Patrick Dean, Katie Ballinger, Victor Martin-Nelson, Kyle Tener, and Sarah Schilling in developing this the python files and scripts. I also received guidance from my instructors
I adapted code from https://github.com/svafaeva93/python-challenge/tree/main to assist and develop my solutions for the challenge. 


Background
It's time to put away the Excel sheet and enter the world of programming with Python. In this assignment, you'll use the concepts you've learned to complete two Python challenges, PyBank and PyPoll. Both tasks present a real-world situation where your newly developed Python scripting skills come in handy.

Before You Begin
Before starting the assignment, be sure to complete the following steps:

Create a new repository for this project called python-challenge. Do not add this homework assignment to an existing repository.

Clone the new repository to your computer.

Inside your local Git repository, create a folder for each Python assignment and name them PyBank and PyPoll.

In each folder that you just created, add the following content:

A new file called main.py. This will be the main script to run for each analysis.

A Resources folder that contains the CSV files you used. Make sure that your script has the correct path to the CSV file.

An analysis folder that contains your text file that has the results from your analysis.

Push these changes to GitHub or GitLab.

Files
Download the following files to help you get started:

Module 3 Challenge filesLinks to an external site.

PyBank Instructions
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

Your analysis should align with the following results:

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
In addition, your final script should both print the analysis to the terminal and export a text file with the results.

PyPoll Instructions
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote

Your analysis should align with the following results:

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
In addition, your final script should both print the analysis to the terminal and export a text file with the results.
