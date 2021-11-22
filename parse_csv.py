import csv
import re

def printDict(mydict):
    for line in mydict:
        print(line)

def csv_to_dict(filename):
    result_list=[]
    with open(filename) as file_obj:
        reader = csv.DictReader(file_obj, delimiter = ',')
        for row in reader:
            #print(row)
            result_list.append(dict(row))
    return result_list

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



def cleanup(mydict):
    row = 0
    rows_to_remove = []
    for line in mydict:
        row = row + 1
        for k,v in line.items():
            # Add rows with empty values to array
            if (v == ''):
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
            

            

# Create a list of dicts
mydict = csv_to_dict('exampledata.csv')
print("before")
printDict(mydict)
cleanup(mydict)
print("after")
printDict(mydict)
#search('25', "Column A", mydict)
