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
    count1 = 0
    count2 = 0
    for line in mydict:
        for k in line:
            if k == 'Column A':
                count1 = count1 + 1
            else:
                count2 = count2 + 1
        #count = count + 1
    
    #print("There are " + str(count) + " elements in the dataset.")
    print("Count        " + str(count1) + "       " + str(count2) + "\n")

def Unique(mydict):
    data1 = [10000]
    data2 = [10000]
    total1 = 0
    total2 = 0
    for line in mydict:
        for k, v in line.items():
            if k == "Column A":
                data1.append(int(v))
            else:
                data2.append(int(v))
    total1 = len(set(data1))
    total2 = len(set(data2))
    print("Unique       " + str(total1) + "        "+ str(total2)+ "\n")
def Mean(mydict):
    count1 = 0
    mean1 = 0
    count2 = 0
    mean2 = 0
    for line in mydict:
        for k, v in line.items():
            if k == 'Column A':
               mean1 = mean1 + int(v)
               count1 = count1 + 1
            else:
               mean2 = mean2 + int(v)
               count2 = count2 + 1
    mean1 = mean1/count1
    mean2 = mean2/count2
    print("Mean         " + str(mean1) + "       " + str(mean2) + "\n")
    
def Median(mydict):
    high = 0
    low = 0
    mid1 = 0
    mid2 = 0
    swap = 0
    for line in mydict:
        for k, v in line.items():
            if k == 'Column A':
                if high == 0:
                    high = v
                elif low == 0:
                    low = v
                elif mid1 == 0:
                    mid1 = v

                if mid1 > low and mid1 < high:
                    continue
                elif high > low and high < mid1:
                    swap = mid1
                    mid1 = high
                    high = swap
                elif low > mid1 and low < high:
                    swap = mid1
                    mid1 = low
                    low = swap
                if low > high:
                    swap = low
                    low = high
                    high = swap
            
            if k == 'Column B':
                if high == 0:
                    high = v
                elif low == 0:
                    low = v
                elif mid2 == 0:
                    mid2 = v

                if mid2 > low and mid2 < high:
                    continue
                elif high > low and high < mid2:
                    swap = mid2
                    mid2 = high
                    high = swap
                elif low > mid2 and low < high:
                    swap = mid2
                    mid2 = low
                    low = swap
                if low > high:
                    swap = low
                    low = high
                    high = swap
    print("Median       " + str(mid1) + "      " + str(mid2) + "\n")

#def Mode(mydict):
    
def SD(mydict):
    mean1 = 0
    count1 = 0
    mean2 = 0
    count2 = 0
    data1 = [10000]
    data2 = [10000]
    tmp = 0
    for line in mydict:
        for k, v in line.items():
            if k == 'Column A':
               mean1 = mean1 + int(v)
               count1 = count1 + 1
            else:
               mean2 = mean2 + int(v)
               count2 = count2 + 1
    mean1 = mean1/count1
    mean2 = mean2/count2
    for line in mydict:
        for k, v in line.items():
            if k == 'Column A':
                tmp = int(v) - mean1
                tmp = tmp * tmp
                data1.append(tmp)
                count1 = count1 + 1
            else:
                tmp = int(v) - mean2
                tmp = tmp * tmp
                data2.append(tmp)
                count2 = count2 + 1
    mean1 = 0
    mean2 = 0
    for i in range(len(data1)):
        mean1 = mean1 + data1[i]
    for i in range(len(data2)):
        mean2 = mean2 + data2[i]
    mean1 = mean1/count1
    mean2 = mean2/count2
    sd1 = mean1**(.5)
    sd2 = mean2**(.5)
    print("SD          " + str(sd1) + "  " + str(sd2) + "\n")
    
def Minimum(mydict):
    minimum1 = 0
    start1 = 0
    minimum2 = 0
    start2 = 0
    for line in mydict:
        for k, v in line.items():
            if k == "Column A":
                if start1 == 0:
                    minimum1 = int(v)
                    start1 = start1 + 1
                if int(v) < minimum1:
                    minimum1 = int(v)
            else:
                if start2 == 0:
                    minimum2 = int(v)
                    start2 = start2 + 1
                if int(v) < minimum2:
                    minimum2 = int(v)
    print("Minimum      " + str(minimum1) + "          " + str(minimum2) + "\n");
    
def Maximum(mydict):
    maximum1 = 0
    start1 = 0
    maximum2 = 0
    start2 = 0
    for line in mydict:
        for k, v in line.items():
            if k == "Column A":
                if start1 == 0:
                    maximum1 = int(v)
                    start1 = start1 + 1
                if int(v) > maximum1:
                    maximum1 = int(v)
            else:
                if start2 == 0:
                    maximum2 = int(v)
                    start2 = start2 + 1
                if int(v) > maximum2:
                    maximum2 = int(v)
    print("Maximum      " + str(maximum1) + "      " + str(maximum2) + "\n");

def Descriptor():
    print("Descriptor   Column A    Column B")
    print("**********   ********    ********")

def dataSummary(mydict):
    Count(mydict)
    Mean(mydict)
    Median(mydict)
    SD(mydict)
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
            Descriptor()
            Count(mydict)
        except:
            print("Error occured\n\n")
        continue
    if (option == 5):
        Descriptor()
        Unique(mydict)
        continue
    if (option == 6):
        try:
            Descriptor()
            Mean(mydict)
        except:
            print("Error occured\n\n")
        continue
    if (option == 7):
        try:    
            Descriptor()
            Median(mydict)
        except:
            print("Error occured\n\n")
        continue
    if (option == 8):
        continue
    if (option == 9):
        try:
            Descriptor()
            SD(mydict)
        except:
            print("Error occured\n\n")
        continue
    if (option == 10):
        continue
    if (option == 11):
        try:
            Descriptor()
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
            Descriptor()
            Maximum(mydict)
        except:
            print("Error occured\n\n")
        continue
    if (option == 18):
        #try:
        Descriptor()
        dataSummary(mydict)
        #except:
         #   print("Error occured\n\n")
        #continue
