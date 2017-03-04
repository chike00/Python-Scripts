"""
This file allows you to pass an list into a function which will put this into an Excel spreadsheet for you. You can change the array
contents and also you can change the names of the columns (the t1, t2, t3 parameters)
"""

import csv #imports csv module
import sys #imports sys module, not necessary but allows you to make custom error messages with sys.stdout.write("...")

names = ["PersonA", "Person B", "Person C", "Person D", "Person E"] #python list which contains arbitrary names
addresses = ["66 Northridge Road", "182 South Thames St.", "101 Random Road", "82 Nigel Road", "44 Christoph Avenue"] #python list which contains addresses
gender = ["female", "male", "male", "male", "female"] #python list which contains the genders of the people


def createSpreadsheet(t1, t2, t3, array1, array2, array3): #createSpreadsheet function with parameters t1, t2, t3, array1, array2 and array3
    #t1, t2 and t3 are the titles of the 1st, 2nd and 3rd columns respectively
    #array1, array2 and array3 are the lists which you pass into the function
    sesame = open('Automated Spreadsheet.csv', 'w') #opens writable file
    sesame.write("{}, {}, {}\n\n".format(t1, t2, t3)) #write the column titles to file
    for x, y, z in zip(array1, array2, array3): #iterates through each list
        sesame.write('{}, {}, {}\n'.format(x, y, z))
    sesame.close() #closes file

createSpreadsheet("name", "address", "gender", names, addresses, gender) #calls functions with column names and array variables passed in
