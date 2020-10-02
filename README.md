# Election_Analysis

## Election Audit Overview
The Colorado Board of Elections requested an election audit to be performed after all votes were cast. The specific requests for this audit are as follows:
  1. Calculate the total number of votes cast. 
  2. Get a complete list of candidates who recieved votes.
  3. Calculate the total number of voters for each candidate.
  4. Calculate the percentage of votes each candidate won.
  5. Determine the winner of the election based on popular vote.
  
## Resources

- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.49.2

## Election Audit Summary

The election analysis shows that:
- There were 369,711 total votes cast

The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
  
The candidate results were:
  - Charles Casper Stockham recieved 23% of the vote with 85,213 votes.
  - Diana DeGette recieved 73.8% of the vote with 272,892 votes.
  - Raymon Anthony Doane recieved 3.1% of the vote with 11,606 votes.
  
The winner of the election was:
  - Diana DeGette who recieved 73.8% of the vote with 85,213 votes.
  
## County Audit Overview
The Colorado Board of Elections requested a summary of voter turnout by county. The counties included in the data were Jefferson County, Denver County, and Arapahoe County. The specific request for this summary was to find:

- Total Number of votes per county.
- Percentage of votes per county.
- The county with the largest amount of votes.

## County Audit Results

The following information was produced by the counties analysis:

- Jefferson County comprised 10.5% of total votes with 38,855 votes.
- Denver County comprised 82.8% of total votes with 306,055 votes.
- Arapahoe County comprised 6.7% of total votes with 24,801 votes. 
- Denver had the largest amount of votes.

## County Audit Summary

The script used for this election audit can be refactored for use in most elections. The most obvious example is inserting different csv files with results from other elections. The code for reading csv files could be changed from:
```
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
```
To:
```
with open(variable for file path in os package) as election_data:
    reader = csv.reader(election_data)
```
This would allow the auditor to insert any csv file with election data to run the analysis on. It should be noted that the variable *election_data* can be changed to whatever the auditor selects, so long as the new variable replaces *election_data* throughout the script. Another way to refactor this code for other elections would be to create different variables and index values based on the csv file. For example, if an auditor recieved data with additional columns that listed cities as well as counties, the same code used in the counties analysis could be applied to cities. This would require declaring new variables just under the county variables.





