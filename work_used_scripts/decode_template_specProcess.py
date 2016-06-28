#! /usr/bin/python

import sys
import os
import re
import shutil
import subprocess
import pdb

def processFile(file):
    #pdb.set_trace()
    ORIG_FILE= open(origPath+file, "r")
    DEST_FILE= open(destPath+file, "w")
    line = ORIG_FILE.readline()

    ORIG_FILE.close()
    DEST_FILE.close()

	   

#================================================
province=sys.argv.pop()

province=sys.argv.pop()
if province == "neimeng":
    import temp_list_neimeng as temp_list
    folder = "nm"
elif province == "xizang":
    import temp_list_xizang as temp_list
    folder = "xz"
elif province == "jiangxi":
    import temp_list_jiangxi as temp_list
    folder = "jx"
else:
    print "unknow provinve %s"%(provinve)
    sys.exit()

workPath="/home/libin3/work/openbilling60_cmcc/rating_billing/rating/decode/template"
#print "%s" % (workPath)
origPath=workPath+"/"+province+"/"
destPath=workPath+"/"+province+"_specProcess/"

os.chdir(workPath)
if os.path.isdir(destPath):
   shutil.rmtree(destPath)
os.mkdir(destPath)

for file in temp_list.specProcessTempList:    
   processFile(file)


