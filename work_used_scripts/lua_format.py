#! /usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import os
import sys
import pdb

province=sys.argv.pop()
if province == "neimeng":
    import temp_list_neimeng as temp_list
elif province == "xizang":
    import temp_list_xizang as temp_list
else:
    print "unknow provinve %s"%(provinve)
    sys.exit()

workpath="/home/libin3/CMCC_ZJ/billing/openbilling60_cmcc/rating_billing/rating/decode/template/"
workpath1=workpath
workpath2=workpath
if province == "neimeng":
    workpath1 +="nm/"
    workpath2 +="nm_pretty/"
elif province == "xizang":
    workpath1 += "xz/"
    workpath2 +="xz_pretty/"
else:
    print "unknown province!!!"
    sys.exit()

for temp in temp_list.voiceTempList:
    isfound = False
    for  root, dirs,files in os.walk(workpath1):
            for file in files:
                if file == temp:
                   isfound=True
                   break

    if isfound == False:
       print "%s is not found!!!"%(temp)
       continue

    ORIG_FILE= open(workpath1+temp, "r")
    DEST_FILE= open(workpath2+temp, "w")
    line = ORIG_FILE.readline()
    curForeSpaceNum=0
    nextForeSpaceNum=0
    while line:
        #remove \n 
        enter_pat=re.compile(r"\n")
        if enter_pat.search(line):
            line=enter_pat.sub("", line)

        #skip blank line
        if blank_line_pat=re.compile(r"^\s+$|^$")
            DEST_FILE.write("%s" % (line))
            line = ORIG_FILE.readline()
            continue

        #modify fore space number of next line 
        big_bracket_pat=re.compile(r"{")
        if big_bracket_pat.search(line):
            


        comment_pat=re.compile(r"^\s+//")
        if comment_pat.search(line):
            foreSpaceNum=0

        line = ORIG_FILE.readline()