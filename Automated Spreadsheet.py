import csv
import sys

names = ["ashley", "bob", "chike", "darren", "elizabeth"]
addresses = ["66 Northridge Road", "182 South Thames St.", "66 Pentridge Street", "82 Nigel Road", "44 Christoph Avenue"]
gender = ["female", "male", "male", "male", "female"]


def one(t1, t2, t3, array1, array2, array3):
    sesame = open('Automated Spreadsheet.csv', 'w')
    sesame.write("{}, {}, {}\n\n".format(t1, t2, t3))
    for x, y, z in zip(array1, array2, array3):
        sesame.write('{}, {}, {}\n'.format(x, y, z))
    sesame.close()

one("name", "address", "gender", names, addresses, gender)
