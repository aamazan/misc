# Description: program to relearn file i/o
import csv
import qs.py as qs

name = input("Please enter a name for your .txt: \n")
name += ".txt"
f1 = open(name,"w")


#while str != "0":
#    if str == "0":
#        break
#    else:
#        f1.write(str + "\n")
#        str = input()

#f1.close()
l = [1,1]
for j in range(0,10):
    l.append(l[j]+l[j+1])

with open("csvtest.txt", "w") as csvfile:
    wr = csv.writer(csvfile, delimiter = ',')

    for i in range(0,10):
        wr.writerow(l[i:i+3])
