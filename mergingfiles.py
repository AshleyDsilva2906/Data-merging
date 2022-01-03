import csv 
import pandas as pd 
file1="bright_stars.csv"
file2="Converted_Dwarf_Stars.csv"

d1=[]
d2=[]

with open(file1,"r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        d1.append(i)

with open(file2,"r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        d2.append(i)

h1=d1[0]
h2=d2[0]

p_d1=d1[1:]
p_d2=d2[1:]
h=h1+h2
p_d=[]
for i in p_d1:
    p_d.append(i)

for i in p_d2:
    p_d.append(i)

with open("Total_Stars.csv","w") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(p_d)
    