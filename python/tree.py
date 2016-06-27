#! /usr/bin/python

import sys
import os
import pdb

if len(sys.argv) == 1:
    infile=os.getcwd()
else:
    infile=sys.argv.pop()

    
if not os.path.exists(infile):
   print "%s is not exist!!!" % (infile)
   sys.exit()

if os.path.isfile(infile):
   print "%s " % (infile)
   sys.exit()
elif os.path.isdir(infile):
   for root, dirs, files in os.walk(infile):
       print "%s: "%(root)

       print "    files: "
       for file in files:
           print "         %s " % (file)

       print "    folers: "
       for dir in dirs:
           print "         %s " % (dir)
else:
    print "%s is not valid!!!" %(infile)
       
       


