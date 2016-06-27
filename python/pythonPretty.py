#! /usr/bin/python

import sys
import os
import re
import pdb

g_lastSpaceNum=0
ADD_SPACE_NUM=6

def get_head_space_num(line):
    if m=re.match(r"(\s*)+", line):
       return len(m.group())
       

def pretty(file):
    isPythonfile=False
    if re.search(r"\.py", file): 
       isPythonfile=True

    FileSrc=open(file,"r")
    line=FileSrc.readline()
    if re.search(r"python", line):
       isPythonfile=True

    if re.search(r"^\..*",file):
       isPythonfile=False

    if isPythonfile==False:
       print "%s is not python file" % (file)
       return

    print "%s is in pretty formatting ... " % (file)

    pdb.set_trace()
    if re.match(r"^$", line):
       return
    else:
       curSpaceNum= get_head_space_num(line)
       if curSpaceNum<= g_lastSpaceNum:
          g_lastSpaceNum = curSpaceNum
          return
       else:          


if 1 == len(sys.argv):
    print "no input file!!!"
    sys.exit()

scriptName=sys.argv[0]
file=sys.argv.pop()
while (1):
     if file == scriptName:
        break;

     if not os.path.exists(file):
        print "%s not exist!!!" % (file)
        sys.exit()

     if os.path.isfile(file):
        pretty(file)  
     elif os.path.isdir(file):
          for root, dirs, files in os.walk(file):
              print "[ %s ]: " % (root)
              for file_ in files:
                  pretty(file_)
     else:
        print "invalid file!!!"


     file=sys.argv.pop()

sys.exit()


