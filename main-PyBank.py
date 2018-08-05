#main.py - PyBank Python File
#Import Modules
import os
import csv

#Set a Path for the csv file
csv_path = os.path.join('Resources/budget_data.csv')

#Open the csv file
with open(csv_path, newline="") as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=",")

#I Could not figure out how to complete the following steps after hours of looking at the week's activities for clues of how to (I did miss this week of class) and unfortunately did not get to this assignment in time to address with a TA in class:
#1. Calculate the number of months in the dataset
#2. Calculate the total amount of profit/losses over the entire period
#3. Calculate the percentage of votes each candidate won
#4. Calculate the total number of votes each candidate won
#5. Calculate the winner of the election based on popular vote
#In addition I spent hours on google trying to figure out how to do the above
#I will follow up with a TA on Tuesday to try and get direction here as I want to understand these concepts and complete this assignment. I am also looking into connecting with a Tutor about this week's material.

#Print Title
print("Financial Analysis")
   
#Print a Separator
print("---------------------------")

#Print number of months in the dataset
print("Total Months: ")

#Print total amount of profit/losses over the entire period
print("Total: ")

#Print the average change in profit/losses between months over the entire period
print("Average Change: ")

#Print the greatest increase profits (date and amount) over the entire period
print("Greatest Increase in Profits: ")

#Print the greatest decrease in losses (date and amount) over the entire period
print ("Greatest Decrease in Profits: ")