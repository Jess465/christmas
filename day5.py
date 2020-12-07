import re

with open("day5.txt") as f:
    lines = f.read().splitlines()

for row in lines:
    #print(i)
    for i in range(10):
        if(row[0] == "F"):
            
