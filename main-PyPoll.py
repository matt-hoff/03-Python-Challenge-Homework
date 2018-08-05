#main.py - PyPoll Python File
#Import Modules
import os
import csv

#Set a Path for the csv file
csv_path = os.path.join('Resources/election_data.csv')

#Open the csv file
with open(csv_path, newline="") as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=",")

#I Could not figure out how to complete the following steps after hours of looking at the week's activities for clues of how to (I did miss this week of class) and unfortunately did not get to this assignment in time to address with a TA in class:
#1. Calculate the total number of votes cast
#2. Calculate the a complete list of candidates who received votes
#3. Calculate the average change in profit/losses between months over the entire period
#4. Calculate the greatest increase profits (date and amount) over the entire period
#5. Calculate the greatest decrease in losses (date and amount) over the entire period
#In addition I spent hours on google trying to figure out how to do the above
#I will follow up with a TA on Tuesday to try and get direction here as I want to understand these concepts and complete this assignment. I am also looking into connecting with a Tutor about this week's material.

#Print Title
print("Election Results ")
   
#Print a Separator
print("---------------------------")

#Print number of months in the dataset
print("Total Votes: ")

#Print a Separator
print("---------------------------")

#Print candidate Kahn's vote percentage and count
print("Kahn: ")

#Print candidate Correy's vote percentage and count
print("Correy: ")

#Print candidate Li's vote percentage and count
print("Li: ")

#Print candidate O'Tooley's vote percentage and count
print("O'Tooley: ")

#Print a Separator
print("---------------------------")

#Print the winning candidate's name
print("Winner: ")

#Print a Separator
print("---------------------------")
