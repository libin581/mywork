#! /usr/bin/python
import sys
import re
import pdb

pdb.set_trace()

file="cdays-4-test.txt"
FILE_R=open(file, "r");
FILE_W=open("result.txt", "w");
    
line=FILE_R.readline()
while line:
    if (re.search(r"^\s*\n$", line)) or (re.search(r"\s*#.*", line)):
       line=FILE_R.readline() 
       continue


    FILE_W.write(line)
    line=FILE_R.readline() 

FILE_R.close()
FILE_W.close()


