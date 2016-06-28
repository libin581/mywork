#! /usr/bin/python

import subprocess
import os
import sys
import re
import pdb

convertFuncNameWithSnapshot=[]
workPath="/home/libin3/CMCC_ZJ/billing/openbilling60_cmcc/rating_billing/rating/decode/tuning/ng/"
headfile="convert_common.h"
sourcefile="convert_common.cpp"
sourcefilenew="convert_common.cpp.new"

if os.path.exists(workPath+sourcefilenew):
    os.remove(workPath+sourcefilenew)

HEAD_FILE= open(workPath+headfile, "r")
SOURCE_FILE= open(workPath+sourcefile, "r")
SOURCE_FILE_NEW= open(workPath+sourcefilenew, "w")

#----get convert function with snapshot list
snapshot_pat=re.compile(r"xc::CSnapshot&\s+snapShot")
function_name_pat=re.compile(r"\w+\(")
line = HEAD_FILE.readline()
while(line):
    if snapshot_pat.search(line):
        if function_name_pat.search(line):
            (start,end)=function_name_pat.search(line).span()
            convertFuncNameWithSnapshot.append(line[start:end-1])
    line = HEAD_FILE.readline()
HEAD_FILE.close()

#----modify source code
#pdb.set_trace()
line = SOURCE_FILE.readline()
func_end = re.compile(r"\)\s*\n$")
func_pat = re.compile(r"int32\s+\w+\(")
while(line):
    if func_pat.search(line):
        isfound=False
        for funcname in convertFuncNameWithSnapshot:
            funcname_pat=re.compile(r"%s"%(funcname))
            if funcname_pat.search(line):
                isfound=True
                break

        if isfound == True:
            if not snapshot_pat.search(line):
                if func_end.search(line):
                    start=func_end.search(line).start()
                    part1=line[:start]
                    part2=line[start:]
                    line=part1+",xc::CSnapshot& snapShot"+part2

    SOURCE_FILE_NEW.write("%s" % (line))
    line = SOURCE_FILE.readline()
SOURCE_FILE.close()
SOURCE_FILE_NEW.close()