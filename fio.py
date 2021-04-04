# Description: program to relearn file i/o
import csv

name = input("Please enter a name for your .txt: \n")
name += ".txt"
f1 = open(name,"w")
str = input("Please enter text for the test document. Type 0 and hit enter to quit. \n")

while str != "0":
    if str == "0":
        break
    else:
        f1.write(str + "\n")
        str = input()

f1.close()

#f2 = open("csvtest.txt", "w")
