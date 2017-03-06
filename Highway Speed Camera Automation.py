#Chike Nwaenie - OCR A453 Computing Coursework, completed 19/03/2016 - 23:26pm

import random #imports random module
import string #imports string module
import os #imports os module
import time #imports time module

print("""In the UK most vehicle registrations are in the format:
    \n\t• Two letters\n\t• Two numbers\n\t• Three letters
    \nFor example, AZ01 XYZ\n""") #alerts the user to the UK plate format

time.sleep(2.5) #uses time module in order to freeze the program

def randomchar1(a): #defining of my function, named randomchar1, with the argument a.
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(a))
"""return is responsible for usually ending a class and passing back
a value when the function is called.

the join method puts strings together conveniently, and random choice with the
string.ascii_uppercase + string.digits, generates a random string
with a combination of letters and numbers which don't have annoying commas
between characters

Next I used for x in range, which tells it do do something in a specific range of numbers,
in the parentheses I placed the parameter a, which currently doesn't have a particular
value as of YET."""

def randomchar15(a): #defining of my function, named randomchar1, with the argument a.
    return ''.join(random.choice(string.ascii_uppercase) for x in range(a))
#function to produce random uppercase letters

def randomchar2(a): #defining of my function, named randomchar1, with the argument a.
    return ''.join(random.choice(string.digits) for x in range(a))
#function to produce random numbers

minutes1 = random.randrange(2, 50)#creates a random number between 2 and 50
minutes2 = random.randrange(2, 50)#creates a random number between 2 and 50
minutes3 = random.randrange(2, 50)#creates a random number between 2 and 50
minutes4 = random.randrange(2, 50)#creates a random number between 2 and 50
minutes5 = random.randrange(2, 50)#creates a random number between 2 and 50

plate1 = str((randomchar1(4) + " " + randomchar1(3)))
plate2 = str((randomchar15(2) + randomchar2(2) + " " + randomchar15(3)))
plate3 = str((randomchar1(4) + " " + randomchar1(3)))
plate4 = str((randomchar15(2) + randomchar2(2) + " " + randomchar15(3)))
plate5 = str((randomchar1(4) + " " + randomchar1(3)))
"""These 5 variables use my pre-made functions in order to specify the length
of my licence plate"""

hours1 = round(minutes1 * 0.0166666667, 2) #makes hours by multiplying by (1/60)
speed1 = round(10/hours1, 2)#makes speed by dividing my distance by time

hours2 = round(minutes2 * 0.0166666667, 2)#makes hours by multiplying by (1/60)
speed2 = round(10/hours2, 2)#makes speed by dividing my distance by time

hours3 = round(minutes3 * 0.0166666667, 2)#makes hours by multiplying by (1/60)
speed3 = round(10/hours3, 2)#makes speed by dividing my distance by time

hours4 = round(minutes4 * 0.0166666667, 2)#makes hours by multiplying by (1/60)
speed4 = round(10/hours4, 2)#makes speed by dividing my distance by time

hours5 = round(minutes5 * 0.0166666667, 2)#makes hours by multiplying by (1/60)
speed5 = round(10/hours5, 2)#makes speed by dividing my distance by time

person1 = ["Anna", plate1, speed1] #puts a name, licence plate and speed into a driver list
person2 = ["Bellamy", plate2, speed2] #puts a name, licence plate and speed into a driver list
person3 = ["Cameron", plate3, speed3] #puts a name, licence plate and speed into a driver list
person4 = ["Darius", plate4, speed4] #puts a name, licence plate and speed into a driver list
person5 = ["Eugene", plate5, speed5] #puts a name, licence plate and speed into a driver list

print(person1[0])#prints name
print(person1[1])#prints licence plate
print(person1[2])#prints speed
print(len(person1[1]))#prints the length of the string
print("\n")#causes Python to print out a newline
print(person2[0])#prints name
print(person2[1])#prints licence plate
print(person2[2])#prints speed
print(len(person2[1]))#prints the length of the string
print("\n")#causes Python to print out a newline
print(person3[0])#prints name
print(person3[1])#prints licence plate
print(person3[2])#prints speed
print(len(person3[1]))#prints the length of the string
print("\n")#causes Python to print out a newline
print(person4[0])#prints name
print(person4[1])#prints licence plate
print(person4[2])#prints speed
print(len(person4[1]))#prints the length of the string
print("\n")#causes Python to print out a newline
print(person5[0])#prints name
print(person5[1])#prints licence plate
print(person5[2])#prints speed
print(len(person5[1]))#prints the length of the string
print("\n")#causes Python to print out a newline
print("Writing cars with non-standard plates AND exceed speed limit, if any...")
#prints message informing viewer that information, if applicable, is being written to file

def write(): #defines my 'write' function
    try:
      path = 'C:' #sets the desired directory
      filename = "file" #names the file
      fullname = os.path.join(path, filename+".txt")#creates the path, makes file .txt format
      
      fw = open(fullname, 'w')  # Trying to create a new file or open one
  
      if str.isalpha(person1[1][0:1]) == False or str.isdigit(person1[1][2:3]) == False or str.isalpha(person1[1][5:7]) == False or len(person1[1]) != 8 or " " not in person1[1][0:]:
          #multiple conditions, if any are met then carry out a consequence
          if person1[2] > 70: #if speed exceeds 70
              fw.write("Driver: " + person1[0])#writes driver name to file
              fw.write("\nStandard Plate? " + "NO - " + person1[1])#writes that plate is not standard
              fw.write(" | Speed exceeds 70mph? YES - " + str(person1[2]) + "mph\n")
              #writes that speed exceeds 70
  
      if str.isalpha(person2[1][0:1]) == False or str.isdigit(person2[1][2:3]) == False or str.isalpha(person2[1][5:7]) == False or len(person2[1]) != 8 or " " not in person2[1][0:]:
          #multiple conditions, if any are met then carry out a consequence
          if person2[2] > 70: #if speed exceeds 70
              fw.write("Driver: " + person2[0])#writes driver name to file
              fw.write("\nStandard Plate? " + "NO - " + person2[1])#writes that plate is not standard
              fw.write(" | Speed exceeds 70mph? YES - " + str(person2[2]) + "mph\n")
              #writes that speed exceeds 70
  
      if str.isalpha(person3[1][0:1]) == False or str.isdigit(person3[1][2:3]) == False or str.isalpha(person3[1][5:7]) == False or len(person3[1]) != 8 or " " not in person3[1][0:]:
          #multiple conditions, if any are met then carry out a consequence
          if person3[2] > 70: #if speed exceeds 70
              fw.write("Driver: " + person3[0])#writes driver name to file
              fw.write("\nStandard Plate? " + "NO - " + person3[1])#writes that plate is not standard
              fw.write(" | Speed exceeds 70mph? YES - " + str(person3[2]) + "mph\n")
              #writes that speed exceeds 70
  
      if str.isalpha(person4[1][0:1]) == False or str.isdigit(person4[1][2:3]) == False or str.isalpha(person4[1][5:7]) == False or len(person4[1]) != 8 or " " not in person4[1][0:]:
          #multiple conditions, if any are met then carry out a consequence
          if person4[2] > 70: #if speed exceeds 70
              fw.write("Driver: " + person4[0])#writes driver name to file
              fw.write("\nStandard Plate? " + "NO - " + person4[1])#writes that plate is not standard
              fw.write(" | Speed exceeds 70mph? YES - " + str(person4[2]) + "mph\n")
              #writes that speed exceeds 70
  
      if str.isalpha(person5[1][0:1]) == False or str.isdigit(person5[1][2:3]) == False or str.isalpha(person5[1][5:7]) == False or len(person5[1]) != 8 or " " not in person5[1][0:]:
          #multiple conditions, if any are met then carry out a consequence
          if person5[2] > 70: #if speed exceeds 70
              fw.write("Driver: " + person5[0])#writes driver name to file
              fw.write("\nStandard Plate? " + "NO - " + person5[1])#writes that plate is not standard
              fw.write(" | Speed exceeds 70mph? YES - " + str(person5[2]) + "mph")
              #writes that speed exceeds 70
              
      fw.close()#closes the text file
    except FileNotFoundError:
      print("\n>>>We could not complete this program due to the specified drive not being found on your computer.")
    
write()#calls the function

#ends the function
