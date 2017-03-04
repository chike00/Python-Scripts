"""
This file uses the os module and shutil module to create files and move them into other folders which you can specify.
"""

import os
import shutil

for i in range(1, 11):
    sesame = open("Automated File 0{}.txt".format(i), 'w')
    sesame.write("Placeholder text")
    sesame.close()

class Automate():
    def createFolders():
        for i in range(1, 11):
            os.mkdir("Automated Folder 0{}".format(i))

    def moveFileToFolder():
        source = os.getcwd()
        file = os.listdir()

        for i in range(1, 11):
            if file[i].endswith(".txt"):
                shutil.move("Automated File 0{}.txt".format(i), "Automated Folder 0{}".format(i))
            
Automate.createFolders()
Automate.moveFileToFolder()
