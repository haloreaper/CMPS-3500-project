# Course: CMPS 3500
# Class Project
# Python Implementation of a custom statistics summary calculator
# Date: 11/21/21
# Student 1: Matthew Taylor
# Student 2: Daisy Cortez
# Student 3: Joseph Gaede
# Description: Data Loading, Cleaning, Searching, and Implementation of statistics summary calculator


import csv
import re

# Iterates through a list of dicts and prints each line
def printDict(mydict):
    for line in mydict:
        print(line)

# Creates a list of dicts from a csv file
def csv_to_dict(filename):
    result_list=[]
    with open(filename) as file_obj:
        reader = csv.DictReader(file_obj, delimiter = ',')
        for row in reader:
            #print(row)
            result_list.append(dict(row))
    return result_list

# Takes a value(element), a key(column), and a dict as parameters for searching
def search(element, column, mydict):
    count = 0
    row = 0
    details = []
    if (column == "DataSet"):
        for line in mydict:
            row = row + 1
            for value in line:
                if (line[value] == element):
                    count = count + 1
                    details.append(str(value) + " row " + str(row))
    else:
        for line in mydict:
            row = row + 1
            for k, v in line.items():
                if (k == column):
                    if (v == element):
                        count = count + 1
                        details.append(str(k) + " row " + str(row))
    print(str(element) + " is present " + str(count) + " times in " + str(column) + ".")
    print("")
    if (count > 0):
        print("Details:\n*********************************\n")
        for i in range(0, len(details)):
            print(str(element) + " is present in " + details[i])


# Does most of the cleanup related things, removes empty and missing rows first
# Then removes keys/columns with non-numerical data
# Finally removes rows with duplicated numbers within the row

def cleanup(mydict):
    row = 0
    rows_to_remove = []
    for line in mydict:
        row = row + 1
        for k,v in line.items():
            # Add rows with empty and None values to array
            if v == '' or v == None:
                rows_to_remove.append(line)
    
    # Iterate through array of empty value rows and delete them
    for i in range(0, len(rows_to_remove)):
        if rows_to_remove[i] in mydict:
            mydict.remove(rows_to_remove[i])

    row = 0
    rows_to_remove = []
    # Iterate through each line in mydict
    for line in mydict:
        row = row + 1
        # Iterate through each key value pair in each line
        for k,v in line.items():
            # Replace all non-numerical values with an empty string
            v = re.sub('[^\d]','',v)
            if v == '':
                # Remove the key from the current line if it contains an empty string value
                line.pop(k, None)
        
        values = list(line.values())
        # Find the lines that have duplicated values
        if len(values) != len(set(values)):
            #print("dupes")
            rows_to_remove.append(line)
    
    # Iterate through array of rows with duplicates and delete them
    for i in range(0, len(rows_to_remove)):
        if rows_to_remove[i] in mydict:
            mydict.remove(rows_to_remove[i])



# Main functions

option = -1

while (option != 0):
    print("Type one of the options below and hit enter\n")
    print("Options:")
    print("1 - Type in a csv file to get data from and clean")
    print("2 - Type in a value to search for and column to search in")
    print("3 - Print the previously load csv file")
    print("0 - Quit")

    option = input("Enter an option...\n")
    
    if (option == 1):
        # Input has to be surrounded byt single quotes for now
        csv_choice = input("Type the file you wish to load 'filename.csv'\n");
        csv_choice = str(csv_choice)
        try:
             mydict = csv_to_dict(csv_choice)
             cleanup(mydict)
             print("Data loaded and cleaned\n\n")
        except:
            print("Error occured\n\n")
        continue
    if (option == 2):
        # no single quotes needed for number input
        search_choice1 = input("Enter the number you want to search for\n")
        search_choice1 = str(search_choice1)
        # single quotes needed again for column name
        search_choice2 = input("Enter the column name you want to search in, or enter 'DataSet' to search the entire cleaned csv file\n\n")
        search_choice2 = str(search_choice2)
        try:
            search(search_choice1, search_choice2, mydict)
        except:
            print("Error occured\n\n")
        continue
    if (option == 3):
        printDict(mydict)
        continue





