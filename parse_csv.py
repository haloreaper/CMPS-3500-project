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
    keys_to_remove = []
    for line in mydict:
        row = row + 1
        # Get list of keys from first dict in list of dicts
        once = 1
        while (once):
            key_list = line.keys()
            #print(key_list)
            once = 0
        val_list = line.values()
        #print("before")
        #print(val_list)

        for k,v in line.items():
            #print(k,v)
            if (v == ''):
                #print(k,v)
                #print(line)
                rows_to_remove.append(line)
    for i in range(0, len(rows_to_remove)):
        #print(mydict[i])
        if rows_to_remove[i] in mydict:
            #print(rows_to_remove[i])
            mydict.remove(rows_to_remove[i])
        
        #for i in range(0, len(val_list)):
            #val_list[i] = re.sub('[^\d]','', val_list[i])
            #if (val_list[i] == ''):
                #print("Row number for " + str(val_list[i]) + " is " + str(row))
                #rows_to_remove.append(row)
    #for i in range(0, len(rows_to_remove)):
        #print(rows_to_remove[i])
        #print(mydict[rows_to_remove[i] - 1])
        #del mydict[rows_to_remove[i] - 1 - i]


# Create a list of dicts
mydict = csv_to_dict('exampledata.csv')
print("before")
printDict(mydict)
cleanup(mydict)
print("after")
printDict(mydict)
#search('25', "Column A", mydict)
