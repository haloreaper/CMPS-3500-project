# Course: CMPS 3500
# Class Project
# Python Implementation of a custom statistics summary calculator
# Date: 11/21/21
# Student 1: Matthew Taylor
# Student 2: Daisy Cortez
# Student 3: Joseph Gaede
# Description: Data Loading, Cleaning, Searching, and Implementation of statistics summary calculator

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
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
# Finally removes duplicate rows

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
    
    # Iterate through lines in mydict while adding non duplicates to new array
    res = []
    for line in mydict:
        if line not in res:
            res.append(line)
    # Sets mydict to the list of no duplicates
    mydict[:] = list(res)

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
    
    print("Count"+"{:11s}".format(" "),end='')
    # reads in values for v in line.items() as long as mydict is not at the end appends
    # them to the data list. executes a number of times equal to the size of numkeys
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
        # sets count equal to the size of the current column
        count = len(data)
        print("{:18s}".format(str(count)),end='')
       
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

    print("Unique"+"{:10s}".format(" "),end='')
    # reads in values for v in line.items() as long as mydict is not at the end appends
    # them to the data list. executes a number of times equal to the size of numkeys 
    for i in range(numkeys):
        for line in mydict:
            for k, v in line.items():
                if k == keys[i]:
                    data.append(float(v))
        
        # prints the number of unique values that are in the current column
        # len(set(data)) removes all duplicates
        print("{:18s}".format(str(len(set(data)))),end='')

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
    print("Mean"+"{:12}".format(" "),end='')
    
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
        print("{:18s}".format(str(round(mean,4))),end='')

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
    print("Median"+"{:10s}".format(" "),end='')
    
    # reads in values from List up to the size of length and appends them to data. 
    # it will execute this a number of times equal to the len(keys)
    for i in range(len(keys)):
        for j in range(int(length)):
            data.append(List[count])
            count = count + 1  
        
        # checks to see where the middle of data is, after that it sets
        # median equal to that value
        if len(data)%2 == 0:
            median = data[int(len(data)/2)]
        else:
            median = data[int(round(len(data)/2))]

        print("{:18s}".format(str(median)),end='')
        
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
    print("Mode"+"{:12s}".format(" "),end='')
    
    # reads in values from List up to the size of length and appends them to data. 
    # it will execute this a number of times equal to the len(keys)
    for i in range(numkeys):
        for j in range(int(length)):
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
            print("{:18s}".format(str(data[index])),end='')
        else:
            print("{:18s}".format("no mode"),end='')

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
    print("Variance"+"{:8s}".format(" "),end='')
    
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
        print("{:18s}".format(str(round(variance,4))),end='')

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
    print("SD"+"{:14s}".format(" "),end='')
    
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
        print("{:18s}".format(str(round(sd,4))),end='')

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
    print("Minimum"+"{:9s}".format(" "),end='')
    
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
        print("{:18s}".format(str(minimum)),end='')

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
    print("P" + str(int(P*100))+"{:13s}".format(" "),end='')
    
    # reads in values for v in line.items() as long as mydict is not at the end appends
    # them to the data list. executes a number of times equal to the size of numkeys
    for i in range(len(keys)):
        for j in range(int(length)):
            data.append(List[count])
            count = count + 1
        index = len(data) * P
        percentile = data[int(index)]
        print("{:18s}".format(str(percentile)),end='')
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
    print("Maximum"+"{:9s}".format(" "),end='')
    
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
        print("{:18s}".format(str(maximum)),end='')
        
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
    print("Descriptor"+"{:6s}".format(" "),end='')
    
    # prints the name of each column
    for i in range(numkeys):
        print(keys[i] + "{:10s}".format("   "),end='')
    
    print("")
    print("**********"+"{:6s}".format(" "),end='')
    
    # prints a number of asterisks equal to the length
    # of the name of the column
    for i in range(numkeys):
        asterisk = '*'
        for j in range(len(keys[i])-1):
            asterisk = asterisk + '*'
        print(asterisk,end='')
        print("{:10s}".format(" "),end='')
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

# Modified this to be a gui based and no longer a menu
# that is displayed on the terminal but the defintions below 
# are for the buttons that are clicked on the gui.  

mydict = csv_to_dict(str('InputDataSample.csv'))
global data 

def option1():       
    
    try:
        cleanup(mydict)
        global data
        data = Sort(mydict)
        messagebox.showinfo("Message","Data loaded and cleaned")

    except:
        messagebox.showinfo("Error","Error occured")
        

# search csv
def option2():
    # no single quotes needed for number input
    search_choice1 = input("Enter the number you want to search for\n")
    search_choice1 = str(search_choice1)
    # single quotes needed again for column name
    search_choice2 = input("Enter the column name you want to search in, or enter 'DataSet' to search the entire cleaned csv file\n\n")
    search_choice2 = str(search_choice2)
    try:
        search(search_choice1, search_choice2, mydict)
        print("")
    except:
        messagebox.showinfo("Error","Error occured")
    
# print csv contents
def option3():
    printDict(mydict)
    print("")  

#count
def option4():
    try:
        Descriptor(mydict)
        Count(mydict)
        print("")
    except:
       messagebox.showinfo("Error","Cannot calculate the count.")
           
# unique
def option5():
    try:
        Descriptor(mydict)
        Unique(mydict)
        print("")

    except:
        messagebox.showinfo("Error","Cannot find the unique.")
        
    
    # mean
def option6():
    try:
        Descriptor(mydict)
        Mean(mydict)
        print("")
    except:
        messagebox.showinfo("Error","Cannot calculate mean.")

#median
def option7():
    try: 
        Descriptor(mydict)
        Median(mydict,data)
        print("")
    except:
        messagebox.showinfo("Error","Cannot calculate median.")

# mode
def option8(): 
    try:
        Descriptor(mydict)
        Mode(mydict,data)
        print("")
    except:
        messagebox.showinfo("Error","Cannot calculate the mode.")

    
# standarad deviation
def option9():
    try:
        Descriptor(mydict)
        SD(mydict)
        print("")
    except:
        messagebox.showinfo("Error","Cannot calculate the standard deviaton.")
 
# variance
def option10():
    try:
        Descriptor(mydict)
        Variance(mydict)
        print("")
    except:
       messagebox.showinfo("Error","Cannot calculate the variance.")


# minimum
def option11():
    try:
        Descriptor(mydict)
        Minimum(mydict)
        print("")
    except:
        messagebox.showinfo("Error","Cannot calculate the minimum.")

# P20
def option12():
    try:
        Descriptor(mydict)
        Percentile(mydict,.20,data)
        print("")
    except:
        messagebox.showinfo("Error","Cannot calculate the 20th percentile.")

    

# P40
def option13():
    try:
        Descriptor(mydict)
        Percentile(mydict,.40,data)
        print("")
    except:
        messagebox.showinfo("Error","Cannot calculate the 40th percentile.")


# P50
def option14():
    try:
        Descriptor(mydict)
        Percentile(mydict,.50,data)
        print("")
    except:
        messagebox.showinfo("Error","Cannot calculate the 50th percentile.")

# P60
def option15():
    try:
        Descriptor(mydict)
        Percentile(mydict,.60,data)
        print("")
    except:
        messagebox.showinfo("Error","Cannot calculate the 60th percentile.")


# P80
def option16():
    try:
        Descriptor(mydict)
        Percentile(mydict,.80,data)
        print("")
    except:
        messagebox.showinfo("Error","Cannot calculate the 80th percentile.")

# maximum
def option17():
    try:
        Descriptor(mydict)
        Maximum(mydict)
        print("")
    except:
        messagebox.showinfo("Error","Cannot calculate the maximum.")


# data summary
def option18():
    try:
        Descriptor(mydict)
        dataSummary(mydict,data)
        print("")
    except:
        messagebox.showinfo("Error","Cannot calculate the minimum.")

def test_button():
    messagebox.showinfo("Message", "It works")


# The gui potion of the program. 
# main function 
root = Tk()
# Name of the Window 
root.title('CS 3500 Project')
frm = ttk.Frame(root, padding=10)
frm.grid()

# Displays the all the Menu Options on the gui instead of terminal all results still 
# print on the terminal as of now. 
ttk.Label(frm, text="Menu Options:", font= ('Aerial 17 bold italic')).grid(column=1, row=0)
ttk.Label(frm, text="1. Retrieve/clean data from a csv file.  ", font= ('Aerial 12')).grid(column=1, row=3)
ttk.Label(frm, text="2. Search for a variable. ", font= ('Aerial 12')).grid(column=1, row=4)
ttk.Label(frm, text="3. Print loaded data.  ", font= ('Aerial 12')).grid(column=1, row=5)
ttk.Label(frm, text="4. Find the Count. ", font= ('Aerial 12')).grid(column=1, row=6)
ttk.Label(frm, text="5. Find the Unique. ", font= ('Aerial 12')).grid(column=1, row=7)
ttk.Label(frm, text="6. Find the Mean. ", font= ('Aerial 12')).grid(column=1, row=8)
ttk.Label(frm, text="7. Find the Median. ", font= ('Aerial 12')).grid(column=1, row=9)
ttk.Label(frm, text="8. Find the Mode. ", font= ('Aerial 12')).grid(column=1, row=10)
ttk.Label(frm, text="9. Find the Standard Deviation", font= ('Aerial 12')).grid(column=1, row=11)
ttk.Label(frm, text="10. Find the Varaiance.", font= ('Aerial 12')).grid(column=1, row=12)
ttk.Label(frm, text="11. Find the Minimum.", font= ('Aerial 12')).grid(column=1, row=13)
ttk.Label(frm, text="12. Find the 20th Percentile.", font= ('Aerial 12')).grid(column=1, row=14)
ttk.Label(frm, text="13. Find the 40th Percentile.", font= ('Aerial 12')).grid(column=1, row=15)
ttk.Label(frm, text="14. Find the 50th Percentile.", font= ('Aerial 12')).grid(column=1, row=16)
ttk.Label(frm, text="15. Find the 60th Percentile.", font= ('Aerial 12')).grid(column=1, row=17)
ttk.Label(frm, text="16. Find the 80th Percentile.", font= ('Aerial 12')).grid(column=1, row=18)
ttk.Label(frm, text="17. Find the Maximum.", font= ('Aerial 12')).grid(column=1, row=19)
ttk.Label(frm, text="18. Prnt a Data Summary.", font= ('Aerial 12')).grid(column=1, row=20)

# These are all the lines of code for displaying all the buttons on the display 
# and each line of code calls one of the definitons mentioned above. 
ttk.Button(frm, text="Option 1", command= option1).grid(column=3, row=3)
ttk.Button(frm, text="Option 2", command= option2).grid(column=3, row=4)
ttk.Button(frm, text="Option 3", command= option3).grid(column=3, row=5)
ttk.Button(frm, text="Option 4", command= option4).grid(column=3, row=6)
ttk.Button(frm, text="Option 5", command= option5).grid(column=3, row=7)
ttk.Button(frm, text="Option 6", command= option6).grid(column=3, row=8)
ttk.Button(frm, text="Option 7", command= option7).grid(column=3, row=9)
ttk.Button(frm, text="Option 8", command= option8).grid(column=3, row=10)
ttk.Button(frm, text="Option 9", command= option9).grid(column=3, row=11)
ttk.Button(frm, text="Option 10", command= option10).grid(column=3, row=12)
ttk.Button(frm, text="Option 11", command= option11).grid(column=3, row=13)
ttk.Button(frm, text="Option 12", command= option12).grid(column=3, row=14)
ttk.Button(frm, text="Option 13", command= option13).grid(column=3, row=15)
ttk.Button(frm, text="Option 14", command= option14).grid(column=3, row=16)
ttk.Button(frm, text="Option 15", command= option15).grid(column=3, row=17)
ttk.Button(frm, text="Option 16", command= option16).grid(column=3, row=18)
ttk.Button(frm, text="Option 17", command= option17).grid(column=3, row=19)
ttk.Button(frm, text="Option 18", command= option18).grid(column=3, row=20)
# This controls the quit button and will close the program and close the 
# window when the quit button is clicked. 
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=21)

root.mainloop()
