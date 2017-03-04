"""
This file uses the os module and shutil module to create files and move them into other folders which you can specify.
"""

import os
import shutil

for i in range(1, 11):
    sesame = open("Automated File 0{}.txt".format(i), 'w') #opens a file, and will loop over making '..File 01", 02, 03...
    sesame.write("Placeholder text") #writes "Placeholder text" into every file, 
    sesame.close() #closes each file after use to avoid bugs and increase speed

class Automate(): #where my functions will be based
    def createFolders():
        for i in range(1, 11):
            os.mkdir("Automated Folder 0{}".format(i))

    def moveFileToFolder():
        source = os.getcwd()
        file = os.listdir()

        for i in range(13):
            if file[i].endswith(".txt"):
                shutil.move("Automated File 0{}.txt".format(i-2), "Automated Folder 0{}".format(i-2))
            
Automate.createFolders()
Automate.moveFileToFolder()
