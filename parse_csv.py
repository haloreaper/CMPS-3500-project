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

    # Iterate through each line in mydict
    for line in mydict:
        # Iterate through each key value pair in each line
        for k,v in line.items():
            # Replace all non-numerical values with an empty string
            v = re.sub('[^\d]','',v)
            if v == '':
                # Remove the key from the current line if it contains an empty string value
                line.pop(k, None)
         
    # Iterate through array of rows with duplicates and delete them
    res = []
    for line in mydict:
        if line not in res:
            res.append(line)
    #print(mydict)
    mydict[:] = list(res)
    #print("\nAfter\n")
    #print(mydict)

# counts the number of elements in the dataset
def Count(mydict):
    data = []
    numkeys = 0
    keys = []
    # reads in the column values from the dictionary
    for line in mydict:
        for k in line:
            keys.append(k)
    # sets numkeys equal to the number of unique keys
    numkeys = len(set(keys))
   
    # places the unique keys into the keys list
    keys = keys[:numkeys]
    
    print("Count"+"{:7s}".format(" ")),
    # reads in values for v in line.items() as long as mydict is not at the end appends
    # them to the data list. executes a number of times equal to the size of numkeys
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
        # sets count equal to the size of the current column
        count = len(data)
        print("{:14s}".format(str(count))), #+ "       " + str(len(mydict)) + "\n")
       
        # resets data for the next column
        del data[:]
    print("")

# counts the number of unique elements in the dataset
def Unique(mydict):
    data = []
    numkeys = 0
    keys = []
    # reads in the column values from the dictionary
    for line in mydict:
        for k in line:
            keys.append(k)
    # sets numkeys equal to the number of unique keys
    numkeys = len(set(keys))

    #places the unique keys into the keys list
    keys = keys[:numkeys]

    print("Unique"+"{:6s}".format(" ")),
    # reads in values for v in line.items() as long as mydict is not at the end appends
    # them to the data list. executes a number of times equal to the size of numkeys 
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
        
        # prints the number of unique values that are in the current column
        # len(set(data)) removes all duplicates
        print("{:14s}".format(str(len(set(data))))),

        # resets data for the next column
        del data[:]
    print("") 

# calculates the mean of each column in the data set
def Mean(mydict):
    data = []
    numkeys = 0
    keys = []
    mean = 0
    count = 0
    # reads in the column values from the dictionary
    for line in mydict:
        for k in line:
            keys.append(k)
    # sets numkeys equal to the number of unique keys
    numkeys = len(set(keys))

    #places the unique keys into the keys list
    keys = keys[:numkeys]
    print("Mean"+"{:8s}".format(" ")),
    
    # reads in values for v in line.items() as long as mydict is not at the end appends
    # them to the data list. executes a number of times equal to the size of numkeys
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))

        # adds up all of the values from the current column with the mean variable 
        for i in range(len(data)):
            mean = mean + data[i]

        # divides the mean variable by the length of the current column to finish
        # calculating mean and then prints
        mean = mean/len(data)
        print("{:14s}".format(str(round(mean,4)))),

        # rest mean and data
        mean = 0
        del data[:]
    print("") 

# find the median of each column in the data set
def Median(mydict,List):
    data = []
    numkeys = 0
    keys = []
    median = 0
    count = 0
    # reads in the column values from the dictionary
    for line in mydict:
        for k in line:
            keys.append(k)
    # sets numkeys equal to the number of unique keys
    numkeys = len(set(keys))
   
    #places the unique keys into the keys list
    keys = keys[:numkeys]
    
    # divides the length of the list by the length of the keys to get how
    # long each column is
    length = len(List)/len(keys)
    print("Median"+"{:6s}".format(" ")),
    
    # reads in values from List up to the size of length and appends them to data. 
    # it will execute this a number of times equal to the len(keys)
    for i in range(len(keys)):
        for j in range(length):
            data.append(List[count])
            count = count + 1  
        
        # checks to see where the middle of data is, after that it sets
        # median equal to that value
        if len(data)%2 == 0:
            median = data[len(data)/2]
        else:
            median = data[int(round(len(data)/2))]

        print("{:14s}".format(str(median))),
        
        # resets data and median
        del data[:]
        median = 0
    print("")

# determines if there is a mode in each column of the data set
def Mode(mydict,List):
    data = []
    numkeys = 0
    keys = []
    UV = []
    numvalues = 0
    mode = 0
    index = 0
    count = 0
    # reads in the column values from the dictionary
    for line in mydict:
        for k in line:
            keys.append(k)
    
    # sets numkeys equal to the number of unique keys
    numkeys = len(set(keys))
    
    # divides the length of the list by the length of the keys to get how
    # long each column is
    length = len(List)/numkeys
    print("Mode"+"{:8s}".format(" ")),
    
    # reads in values from List up to the size of length and appends them to data. 
    # it will execute this a number of times equal to the len(keys)
    for i in range(numkeys):
        for j in range(length):
            data.append(List[count])
            count = count + 1
        
        # fills UV with 0's
        UV = [0] * len(data)

        # compares every value in data to every value in data, if they match
        # increment the matching index in UV by 1 (keeps track of instances of numbers)
        for j in range(len(data)):
            for k in range(len(data)):
                if data[j] == data[k]:
                    UV[j] = UV[j] + 1

        # cuts data list down so that each value only has 1 instance
        list(set(data))

        # figures out which spot in UV holds the mode index
        for i in range(len(UV)):
            if UV[i] > mode:
                mode = UV[i]
                index = i

        # prints whether there is a mode or not
        if mode > 1:
            print("{:14s}".format(str(data[index]))),
        else:
            print("{:14s}".format("no mode")),

        # resets mode and data
        mode = 0
        del data[:]
    print("")

# calculates the variance of each column in the dataset
def Variance(mydict):
    data = []
    numkeys = 0
    keys = []
    mean = 0
    variance = 0
    tmp = 0
    # reads in the column values from the dictionary
    for line in mydict:
        for k in line:
            keys.append(k)
    
    # sets numkeys equal to the number of unique keys       
    numkeys = len(set(keys))
    
    #places the unique keys into the keys list
    keys = keys[:numkeys]
    print("Variance"+"{:4s}".format(" ")),
    
    # reads in values for v in line.items() as long as mydict is not at the end appends
    # them to the data list. executes a number of times equal to the size of numkeys
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
        
        # calculates the mean of the column
        for i in range(len(data)):
            mean = mean + data[i]
        mean = mean/len(data) 

        # subtracts the mean from each value in the column and squares the difference
        # before adding it to variance
        for i in range(len(data)):
            tmp = data[i] - mean
            tmp = tmp**(2)
            variance = variance + tmp

        # finishes by dividing by length of column
        variance = variance/len(data)
        print("{:14s}".format(str(round(variance,4)))),

        # resets mean, variance, and data
        mean = 0
        variance = 0
        del data[:]
    print("")

# calculates the standard deviation of each column in the dataset
def SD(mydict):
    data = []
    numkeys = 0
    keys = []
    mean = 0
    tmp = 0
    sd = 0
    # reads in the column values from the dictionary
    for line in mydict:
        for k in line:
            keys.append(k)
    
    # sets numkeys equal to the number of unique keys
    numkeys = len(set(keys))
    
    #places the unique keys into the keys list
    keys = keys[:numkeys]
    print("SD"+"{:10s}".format(" ")),
    
    # reads in values for v in line.items() as long as mydict is not at the end appends
    # them to the data list. executes a number of times equal to the size of numkeys
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
        
        # calculates the mean of the column
        for i in range(len(data)):
            mean = mean + data[i]
        mean = mean/len(data) 

        # subtracts the mean from each value in the column, squres the difference, and
        # then stores the values back into the data list
        for i in range(len(data)):
            tmp = data[i] - mean
            tmp = tmp**(2)
            data[i] = tmp

        # resets mean
        mean = 0

        # calculates mean a second time using the new values in data
        for i in range(len(data)):
            mean = mean + data[i]
        mean = mean/len(data)

        # takes the squreroot of the new mean to get standard deviation
        sd = mean**(.5)
        print("{:14s}".format(str(round(sd,4)))),

        # resets mean, sd, and data
        mean = 0
        sd = 0
        del data[:]
    print("") 

# finds the minimum of each column in the data set
def Minimum(mydict):
    data = []
    numkeys = 0
    keys = []
    minimum = 0
    # reads in the column values from the dictionary
    for line in mydict:
        for k in line:
            keys.append(k)

    # sets numkeys equal to the number of unique keys
    numkeys = len(set(keys))
    
    #places the unique keys into the keys list
    keys = keys[:numkeys]
    print("Minimum"+"{:5s}".format(" ")),
    
    # reads in values for v in line.items() as long as mydict is not at the end appends
    # them to the data list. executes a number of times equal to the size of numkeys
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
        
        # compares every value in the column to the value stored in minimum
        # if i is currently 0 then minimum will equal whatever the first value
        # is, otherwise minimum will only change if the new value is less than
        # minimum
        for i in range(len(data)):
            if i == 0:
                minimum = data[i]
            elif data[i] < minimum:
                minimum = data[i]
        print("{:14s}".format(str(minimum))),

        # reset minimum and data
        minimum = 0
        del data[:]
    print("")

# finds the requested percentiles of the columns
def Percentile(mydict,P,List):
    data = []
    numkeys = 0
    keys = []
    median = 0
    index = 0
    percentile = 0
    length = 0
    count = 0
    for line in mydict:
        for k in line:
            keys.append(k)
    
    # sets numkeys equal to the number of unique keys
    numkeys = len(set(keys))
    
    #places the unique keys into the keys list
    keys = keys[:numkeys]
    
    # divides the length of the list by the length of the keys to get how
    # long each column is
    length = len(List)/len(keys)
    print("P" + str(int(P*100))+"{:9s}".format(" ")),
    
    # reads in values for v in line.items() as long as mydict is not at the end appends
    # them to the data list. executes a number of times equal to the size of numkeys
    for i in range(len(keys)):
        for j in range(length):
            data.append(List[count])
            count = count + 1
        # sets index equal to the length of data times the value of P
        # this number should be the percentile we are looking for
        index = len(data) * P
        percentile = data[int(index)]
        print("{:14s}".format(str(percentile))),
        del data[:]
    print("")

# finds the maximum of each column
def Maximum(mydict):
    data = []
    numkeys = 0
    keys = []
    maximum = 0
    # reads in the column values from the dictionary
    for line in mydict:
        for k in line:
            keys.append(k)
    
    # sets numkeys equal to the number of unique keys
    numkeys = len(set(keys))

    #places the unique keys into the keys list
    keys = keys[:numkeys]
    print("Maximum"+"{:5s}".format(" ")),
    
    # reads in values for v in line.items() as long as mydict is not at the end appends
    # them to the data list. executes a number of times equal to the size of numkeys
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
        
        # compares every value in the column to the value stored in maximum.
        # if i is currently 0 then maximum will equal whatever the first value
        # is, otherwise maximum will only change if the new value is greater than
        # maximum
        for i in range(len(data)):
            if i == 0:
                maximum = data[i]
            elif data[i] > maximum:
                maximum = data[i]
        print("{:14s}".format(str(maximum))),
        
        # reset maximum and data
        maximum = 0
        del data[:]
    print("")

# prints the default descriptor that is with each operation
def Descriptor(mydict):
    numkeys = 0
    keys = []
    asterisk = ''
    # reads in the column values from the dictionary
    for line in mydict:
        for k in line:
            keys.append(k)
    
    # sets numkeys equal to the number of unique keys
    numkeys = len(set(keys))
    
    # prints the word descriptor
    print("Descriptor"+"{:2s}".format(" ")),
    
    # prints the name of each column
    for i in range(numkeys):
        print(keys[i] + "{:6s}".format("   ")),
    
    print("")
    print("**********"+"{:2s}".format(" ")),
    
    # prints a number of asterisks equal to the length
    # of the name of the column
    for i in range(numkeys):
        asterisk = '*'
        for j in range(len(keys[i])-1):
            asterisk = asterisk + '*'
        print(asterisk),
        print("{:5s}".format(" ")),
    print("")

# sort function that is called whenever a file is called to be cleaned
def Sort(mydict):
    data = []
    numkeys = 0
    keys = []
    result = []
    # reads in the column values from the dictionary
    for line in mydict:
        for k in line:
            keys.append(k)
    
    # sets numkeys equal to the number of unique keys
    numkeys = len(set(keys))
    
    #places the unique keys into the keys list
    keys = keys[:numkeys]
    
    # reads in values for v in line.items() as long as mydict is not at the end appends
    # them to the data list. executes a number of times equal to the size of numkeys
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
        # sorts the data in the column    
        i = 1
        while i < len(data):
            j = i
            while j > 0 and data[j-1] > data[j]:
                tmp = data[j]
                data[j] = data[j-1]
                data[j-1] = tmp
                j = j -1
            i = i + 1
        
        # appends the sorted values from the column to the result list
        for i in range(len(data)):
            result.append(data[i])

        # resets data
        del data[:]

    # returns the sorted data list
    return result

# calls every statistical operation
def dataSummary(mydict,List):
    Count(mydict)
    Unique(mydict)
    Mean(mydict)
    Median(mydict,List)
    Mode(mydict,List)
    SD(mydict)
    Variance(mydict)
    Minimum(mydict)
    Percentile(mydict,.20,List)
    Percentile(mydict,.40,List)
    Percentile(mydict,.50,List)
    Percentile(mydict,.60,List)
    Percentile(mydict,.80,List)
    Maximum(mydict)
    print("")

# Main functions

option = -1 

# runs until the user types 0
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
    
    # clean csv
    if (option == 1):
        # Input has to be surrounded byt single quotes for now
        csv_choice = input("Type the file you wish to load 'filename.csv'\n");
        csv_choice = str(csv_choice)
        try:
            mydict = csv_to_dict(csv_choice)
            cleanup(mydict)
            data = Sort(mydict)
            print("Data loaded and cleaned\n\n")
        except:
            print("Error occured\n\n")
            continue

    # search csv
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
    # print csv contents
    if (option == 3):
        printDict(mydict)
        continue

    # count
    if (option == 4):
        try:
            Descriptor(mydict)
            Count(mydict)
        except:
            print("Error occured\n\n")
        continue
    
    # unique
    if (option == 5):
        try:
            Descriptor(mydict)
            Unique(mydict)
        except:
            print("Error occured\n\n")
        continue
    
    # mean
    if (option == 6):
        try:
            Descriptor(mydict)
            Mean(mydict)
        except:
            print("Error occured\n\n")
        continue
    
    # median
    if (option == 7):
        try:    
            Descriptor(mydict)
            Median(mydict,data)
        except:
            print("Error occured\n\n")
        continue
    
    # mode
    if (option == 8):
        try:
            Descriptor(mydict)
            Mode(mydict,data)
        except:
            print("Error occured\n\n")
        continue
    
    # standarad deviation
    if (option == 9):
        try:
            Descriptor(mydict)
            SD(mydict)
        except:
            print("Error occured\n\n")
        continue
    
    # variance
    if (option == 10):
        try:
            Descriptor(mydict)
            Variance(mydict)
        except:
            print("Error occured\n\n")
        continue
    
    # minimum
    if (option == 11):
        try:
            Descriptor(mydict)
            Minimum(mydict)
        except:
            print("Error occured\n\n")
        continue
    
    # P20
    if (option == 12):
        try:
            Descriptor(mydict)
            Percentile(mydict,.20,data)
        except:
            print("Error occured\n\n")
        continue
    
    # P40
    if (option == 13):
        try:
            Descriptor(mydict)
            Percentile(mydict,.40,data)
        except:
            print("Error occured\n\n")
        continue
    
    # P50
    if (option == 14):
        try:
            Descriptor(mydict)
            Percentile(mydict,.50,data)
        except:
            print("Error occured\n\n")      
        continue
    
    # P60
    if (option == 15):
        try:
            Descriptor(mydict)
            Percentile(mydict,.60,data)
        except:
            print("Error occured\n\n")    
        continue
    
    # P80
    if (option == 16):
        try:
            Descriptor(mydict)
            Percentile(mydict,.80,data)
        except:
            print("Error occured\n\n")  
        continue
    
    # maximum
    if (option == 17):
        try:
            Descriptor(mydict)
            Maximum(mydict)
        except:
            print("Error occured\n\n")
        continue
    
    # data summary
    if (option == 18):
        try:
            Descriptor(mydict)
            dataSummary(mydict,data)
        except:
            print("Error occured\n\n")
        continue
