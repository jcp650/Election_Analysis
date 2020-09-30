# begin assignment

counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.insert(1, {"county":"El Paso", "registered_voters": 461149})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data.pop(1)
voting_data.insert(2, {"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters")

for county_dict in voting_data:
    print(county_dict['registered_voters'])

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#Skill Drill-- use .items for dictionary key and values
for county, registered_voters in voting_data.items():
    print(f"{county} has {registered_voters:,} registered voters")

import csv
dir(csv)
