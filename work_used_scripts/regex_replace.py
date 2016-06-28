#! /usr/bin/python

import subprocess
import os
import sys
import re
import pdb

def usage():
    scriptName = sys.argv[0]
    print "    =====usage=====\n"
    print "    %s -h                 : help\n"%(scriptName)
    print "    %s -a                 : replace all files\n"%(scriptName)
    print "    %s file1 file2 ...    : replace file1 file2 ...\n"%(scriptName)

fileObjs = []
if len(sys.argv) == 1:
    usage()
elif sys.argv.pop() == "-a":
    for  root, dirs,files in os.walk("./"):
        for file in files:
            fileObjs.append(file)
else:
    for file in sys.argv:
        if file != sys.argv[0]:
            file=sys.argv.pop()
            fileObjs.append(file)
    
for file in fileObjs:
    fileTmp=file+'.tmp'

    ORIG_FILE= open('./'+file, "r")
    DEST_FILE= open('./'+fileTmp, "w")

    comment_pat=re.compile(r"^--|^\s+--")

    orig_str_pat=re.compile(r".+\=\s+string.trim")

    local_pat=re.compile(r"^\s+local")

    line = ORIG_FILE.readline()
    while line:
        comment_search=comment_pat.search(line)
        if comment_search:
            DEST_FILE.write(line)
            line = ORIG_FILE.readline()
            continue
        
        orig_str_search = orig_str_pat.search(line)
        if orig_str_search:
            eq_pat = re.compile(r"=")
            #pdb.set_trace()
            eq_search = eq_pat.search(line)
            if eq_search:
                eq_idx=eq_search.start()
                str1=line[:eq_idx-1]
                word_pat = re.compile(r"\w+")
                words = word_pat.findall(str1)
                if words:
                    word = words[-1]
                    local_search = local_pat.search(line)
                    if local_search:
                        line ="    local "+word+" = string.gsub("+word+", \" \", \"\");\n"
                    else:
                        line = "    "     +word+" = string.gsub("+word+", \" \", \"\");\n"
                else:
                    print "word is not found in: %s\n\n"%(str1)
            else:
                print "\"=\" is not found in line: %s\n\n"%(line)
            
        DEST_FILE.write(line)
        line = ORIG_FILE.readline()
        
    ORIG_FILE.close()
    DEST_FILE.close()

    os.remove(file)
    os.rename(fileTmp,file) 
