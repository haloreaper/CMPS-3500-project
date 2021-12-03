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

# counts how many elements are in the dataset
def Count(mydict):
    data = []
    numkeys = 0
    keys = []
    for line in mydict:
        for k in line:
            keys.append(k)
    numkeys = len(set(keys))
    keys = keys[:numkeys]
    print("Count       "),
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
        count = len(data)
        print("{:11s}".format(str(count))), #+ "       " + str(len(mydict)) + "\n")
        del data[:]
    print("")

def Unique(mydict):
    data = []
    numkeys = 0
    keys = []
    for line in mydict:
        for k in line:
            keys.append(k)
    numkeys = len(set(keys))
    keys = keys[:numkeys]
    print("Unique      "),
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
        print("{:11s}".format(str(len(set(data))))),
        del data[:]
    print("") 

def Mean(mydict):
    data = []
    numkeys = 0
    keys = []
    mean = 0
    count = 0
    for line in mydict:
        for k in line:
            keys.append(k)
    numkeys = len(set(keys))
    keys = keys[:numkeys]
    print("Mean        "),
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
        for i in range(len(data)):
            mean = mean + data[i]
        mean = mean/len(data)
        print("{:11s}".format(str(round(mean,4)))),
        mean = 0
        del data[:]
    print("") 

def Median(mydict):
    data = []
    numkeys = 0
    keys = []
    high = 0
    low = 0
    mid = 0
    tmp = 0
    for line in mydict:
        for k in line:
            keys.append(k)
    numkeys = len(set(keys))
    keys = keys[:numkeys]
    print("Median      "),
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
            #insert sorting algorithm
        for j in range(len(data)):
            if high == 0:
                high = data[i]
            elif mid == 0:
                mid = data[i]
            elif low == 0:
                low = data[i]
            if mid > low and mid < high:
                continue
            elif high > low and high < mid:
                tmp = mid
                mid = high
                high = tmp
            elif low > mid and low < high:
                tmp = mid
                mid = low
                low = tmp
            elif low > high:
                tmp = low
                low = high
                high = tmp
            low = data[j]
        print("{:11s}".format(str(mid))),
        del data[:]
        mid = 0
        high = 0
        low = 0
        median = 0
    print("")

#def Mode(mydict):

def Variance(mydict):
    data = []
    numkeys = 0
    keys = []
    mean = 0
    variance = 0
    tmp = 0
    for line in mydict:
        for k in line:
            keys.append(k)
    numkeys = len(set(keys))
    keys = keys[:numkeys]
    print("Variance    "),
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
        for i in range(len(data)):
            mean = mean + data[i]
        mean = mean/len(data) 
        for i in range(len(data)):
            tmp = data[i] - mean
            tmp = tmp**(2)
            variance = variance + tmp
        variance = variance/len(data)
        print("{:11s}".format(str(round(variance,4)))),
        mean = 0
        variance = 0
        del data[:]
    print("")

def SD(mydict):
    data = []
    numkeys = 0
    keys = []
    mean = 0
    tmp = 0
    sd = 0
    for line in mydict:
        for k in line:
            keys.append(k)
    numkeys = len(set(keys))
    keys = keys[:numkeys]
    print("SD          "),
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
        for i in range(len(data)):
            mean = mean + data[i]
        mean = mean/len(data) 
        for i in range(len(data)):
            tmp = data[i] - mean
            tmp = tmp**(2)
            data[i] = tmp
        mean = 0
        for i in range(len(data)):
            mean = mean + data[i]
        mean = mean/len(data)
        sd = mean**(.5)
        print("{:11s}".format(str(round(sd,4)))),
        mean = 0
        sd = 0
        del data[:]
    print("") 

def Minimum(mydict):
    data = []
    numkeys = 0
    keys = []
    minimum = 0
    for line in mydict:
        for k in line:
            keys.append(k)
    numkeys = len(set(keys))
    keys = keys[:numkeys]
    print("Minimum     "),
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
        for i in range(len(data)):
            if i == 0:
                minimum = data[i]
            elif data[i] < minimum:
                minimum = data[i]
        print("{:11s}".format(str(minimum))),
        minimum = 0
        del data[:]
    print("")

def Maximum(mydict):
    data = []
    numkeys = 0
    keys = []
    maximum = 0
    for line in mydict:
        for k in line:
            keys.append(k)
    numkeys = len(set(keys))
    keys = keys[:numkeys]
    print("Maximum     "),
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
        for i in range(len(data)):
            if i == 0:
                maximum = data[i]
            elif data[i] > maximum:
                maximum = data[i]
        print("{:11s}".format(str(maximum))),
        maximum = 0
        del data[:]
    print("")

def Descriptor(mydict):
    numkeys = 0
    keys = []
    asterisk = ''
    for line in mydict:
        for k in line:
            keys.append(k)
    numkeys = len(set(keys))
    
    print("Descriptor  "),
    
    for i in range(numkeys):
        print(keys[i] + "   "),
    
    print("")
    print("**********  "),
    
    for i in range(numkeys):
        asterisk = '*'
        for j in range(len(keys[i])-1):
            asterisk = asterisk + '*'
        print(asterisk),
        print("  "),
    print("")

def dataSummary(mydict):
    Count(mydict)
    Mean(mydict)
    Median(mydict)
    SD(mydict)
    Variance(mydict)
    Minimum(mydict)
    Maximum(mydict)
    print("")

# Main functions

option = -1 

while (option != 0):
    print("Type one of the options below and hit enter\n")
    print("Options:")
    print("1 - Type in a csv file to get data from and clean")
    print("2 - Type in a value to search for and column to search in")
    print("3 - Print the previously load csv file")
    print("4 - Count")
    print("5 - Unique")
    print("6 - Mean")
    print("7 - Median")
    print("8 - Mode")
    print("9 - Standard Deviation")
    print("10 - Variance")
    print("11 - Minimum")
    print("12 - 20 Percentile")
    print("13 - 40 Percentile")
    print("14 - 50 Percentile")
    print("15 - 60 Percentile")
    print("16 - 80 Percentile")
    print("17 - Maximum")
    print("18 - Data Summary")
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
    if (option == 4):
        try:
            Descriptor(mydict)
            Count(mydict)
        except:
            print("Error occured\n\n")
        continue
    if (option == 5):
        Descriptor(mydict)
        Unique(mydict)
        continue
    if (option == 6):
        try:
            Descriptor(mydict)
            Mean(mydict)
        except:
            print("Error occured\n\n")
        continue
    if (option == 7):
        try:    
            Descriptor(mydict)
            Median(mydict)
        except:
            print("Error occured\n\n")
        continue
    if (option == 8):
        continue
    if (option == 9):
        try:
            Descriptor(mydict)
            SD(mydict)
        except:
            print("Error occured\n\n")
        continue
    if (option == 10):
        try:
            Descriptor(mydict)
            Variance(mydict)
        except:
            print("Error occured\n\n")
        continue
    if (option == 11):
        try:
            Descriptor(mydict)
            Minimum(mydict)
        except:
            print("Error occured\n\n")
        continue
    if (option == 12):
        continue
    if (option == 13):
        continue
    if (option == 14):
        continue
    if (option == 15):
        continue
    if (option == 16):
        continue
    if (option == 17):
        try:
            Descriptor(mydict)
            Maximum(mydict)
        except:
            print("Error occured\n\n")
        continue
    if (option == 18):
        try:
            Descriptor(mydict)
            dataSummary(mydict)
        except:
            print("Error occured\n\n")
        continue
