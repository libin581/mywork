#! /usr/bin/python

import pdb
import sys
import re
import os

#pdb.set_trace()

'''if len(sys.argv) > 1:
    file= sys.argv[1];
else:
    print "no input file!!!\n"
    sys.exit();
'''

workpath="/home/ut/billing/decode";
os.chdir(workpath);

filelist=os.listdir(workpath);

txtpat=re.compile(r"\.txt")
for file in filelist:
    if (txtpat.search(file) == None):
       print "%s is not txt file  \n" % (file)
       continue

    print "%s is in analysis ... \n" % (file)

    FlHandle=open(file)
    line=FlHandle.readline()
    pat = re.compile(r"\$.*</");
    rep = re.compile(r"</.*$");
    dellinefeed = re.compile(r"[\r\n]?$")
    while line:
       match = pat.search(line)
   
       if match:
           mstr=dellinefeed.sub("", match.group());
           mstr=rep.sub("", mstr)
           print "%s" % (mstr)
  
       line=FlHandle.readline()

    FlHandle.close()


