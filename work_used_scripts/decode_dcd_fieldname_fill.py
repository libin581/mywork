#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import re
import shutil
import subprocess
import pdb

def usage():
    print '''
    usage:
    decode_dcd_fieldname_fill.py            : help info
    decode_dcd_fieldname_fill.py -h         : help info
    decode_dcd_fieldname_fill.py --help     : help info
    decode_dcd_fieldname_fill.py *.dcd -c   : check decode template
    decode_dcd_fieldname_fill.py *.dcd -c   : audo fill decode template
    decode_dcd_fieldname_fill.py path       : check and fill all decode templates at this path
    
    eg: 
       1. decode_dcd_fieldname_fill.py file.dcd -c
       2. decode_dcd_fieldname_fill.py file.dcd -f
       3. decode_dcd_fieldname_fill.py ./ -c
    
    note:
    dcd文件应该有完整的FIELD_NAME和FIELD_NEXT_FIELD结构
    脚本的功能是去检查和自动修改FIELD_NAME和FIELD_NEXT_FIELD
    '''
    
dcd_pat=re.compile(r"\.dcd$")
def isDcdFile(fileName):
    if dcd_pat.search(fileName):
        return True
    else:
        return False 
    
comment_line_pat = re.compile(r"^\s*//")
def skipCommentLine(line):
    if comment_line_pat.search(line):
        return True
    else:
        return False
    
#define 正则表达式
RECORD_pat        = re.compile(r"^\s+RECORD\s*\n$|^\s+RECORD\s*\r\n$") #	RECORD
FIELD_NAME_pat    = re.compile(r"^\s+FIELD_NAME\s*=\s*\w+\s*\n$|^\s+FIELD_NAME\s*=\s*\w+\s*\r\n$") #			FIELD_NAME = BEGIN
FIELD_NEXT_FIELD_pat = re.compile(r"^\s+FIELD_NEXT_FIELD\s*=") #			FIELD_NEXT_FIELD =
left_bracket_pat  = re.compile(r"^\s+{")  #	{
right_bracket_pat = re.compile(r"^\s+}")  #	{
RECORD_NAME_pat   = re.compile(r"^\s+RECORD_NAME\s*=\s*\w+\s*\n$|^\s+RECORD_NAME\s*=\s*\w+\s*\r\n$") #			RECORD_NAME = control
ASN_BER_pat           = re.compile(r"ASN|PROPERTY_FILE_ENCODE_TYPE\s*=\s*BER")
var_pat = re.compile(r"\w+")

FIELDNAME_count = {}
def FIELD_NAME_cout(line_list):
    #count FIELD_NAME in RECORD 
    IS_IN_RECORD      = False
    bracket_deep      = 0
    FIELD_NAME_num    = 0
    RECORD_NAME_value = []
    for i, line in enumerate(line_list):
        if skipCommentLine(line) == True:
            continue
           
        if IS_IN_RECORD == False:
            if RECORD_pat.search(line):
                IS_IN_RECORD = True
            continue
        else:
            if left_bracket_pat.search(line):
                bracket_deep += 1
                continue
            if right_bracket_pat.search(line):
                bracket_deep -= 1
                if bracket_deep == 0:
                    IS_IN_RECORD = False
                    if RECORD_NAME_value:
                        FIELDNAME_count[ RECORD_NAME_value] = FIELD_NAME_num
                        FIELD_NAME_num = 0
                        RECORD_NAME_value = []
                    else:
                        print "RECORD_NAME is null!!!"
                        sys.exit()
                continue
            FIELD_NAME_search = FIELD_NAME_pat.search(line)
            if  FIELD_NAME_search:
                FIELD_NAME_num += 1
            RECORD_NAME_search = RECORD_NAME_pat.search(line)
            if RECORD_NAME_search:
                vars = var_pat.findall(line)
                RECORD_NAME_value = vars[-1]
                            
    print
    print "-----RECORD_NAME:  FIELD count-----"
    for FIELD_NAME in FIELDNAME_count.keys():
        print "%s: %d"%(FIELD_NAME, FIELDNAME_count[FIELD_NAME])
    print
    
    
#check all FIELD_NAME and FIELD_NEXT_FIELD
def check_FIELD_NAME(line_list):
    IS_IN_RECORD      = False
    bracket_deep      = 0
    FIELD_NAME_num    = 0
    FIELD_NEXT_FIELD = []
    RECORD_NAME_value = []
    FIELD_count         = 0
    line_count = len(line_list)
    
    print "-----check begin-----"
    
    for i, line in enumerate(line_list):
        if i == (line_count-1):
            print "no error found"
            print
            continue
          
        if ASN_BER_pat.search(line):
            return False
            
        if skipCommentLine(line) == True:
            continue
           
        if IS_IN_RECORD == False:
            if RECORD_pat.search(line):
                IS_IN_RECORD = True
            continue
        else:
            if left_bracket_pat.search(line):
                bracket_deep += 1
                continue
            if right_bracket_pat.search(line):
                bracket_deep -= 1
                if bracket_deep == 0:
                    IS_IN_RECORD      = False
                    bracket_deep      = 0
                    FIELD_NAME_num    = 0
                    FIELD_NEXT_FIELD = []
                    RECORD_NAME_value = []
                continue
                
            if RECORD_NAME_value == []:    
                RECORD_NAME_search = RECORD_NAME_pat.search(line)
                if RECORD_NAME_search:
                    vars = var_pat.findall(line)
                    RECORD_NAME_value = vars[-1]
                    if FIELDNAME_count.has_key(RECORD_NAME_value):
                        FIELD_count = FIELDNAME_count[RECORD_NAME_value]
                    else: 
                        print "RECORD_NAME is not found!!!"
                        sys.exit()
                    continue
                
            FIELD_NAME_search = FIELD_NAME_pat.search(line)
            if  FIELD_NAME_search:
                FIELD_NAME_num += 1
                if not (FIELD_NAME_num == 1):
                    if FIELD_NEXT_FIELD:
                        vars = var_pat.findall(line)
                        FIELD_NAME_value = vars[-1]
                        if not (FIELD_NAME_value == FIELD_NEXT_FIELD):
                            print "line number:%d, FIELD_NAME:%s, FIELD_NEXT_FIELD:%s"%(i+1, FIELD_NAME_value, FIELD_NEXT_FIELD)
                            sys.exit()
                    else:
                        print "FIELD_NEXT_FIELD is null!!!"
                        sys.exit()
                continue
                
            FIELD_NEXT_FIELD_search = FIELD_NEXT_FIELD_pat.search(line)
            if FIELD_NEXT_FIELD_search:
                vars = var_pat.findall(line)
                FIELD_NEXT_FIELD = vars[-1]
                if FIELD_NAME_num == FIELD_count:
                    if not(FIELD_NEXT_FIELD == "NULL"):
                        print "line number:%d, the last FIELD_NEXT_FIELD:%s"%(i+1, FIELD_NEXT_FIELD) 
                        sys.exit()
    
#fill all FIELD_NAME and FIELD_NEXT_FIELD
def fill_FIELD_NAME(line_list):
    IS_IN_RECORD      = False
    bracket_deep      = 0
    FIELD_NAME_num    = 0
    FIELD_NEXT_FIELD = []
    for i, line in enumerate(line_list):
        if skipCommentLine(line) == True:
            continue
           
        if IS_IN_RECORD == False:
            if RECORD_pat.search(line):
                IS_IN_RECORD = True
            continue
        else:
            if left_bracket_pat.search(line):
                bracket_deep += 1
                continue
            if right_bracket_pat.search(line):
                bracket_deep -= 1
                if bracket_deep == 0:
                    IS_IN_RECORD = False
                continue
                
            RECORD_NAME_search = RECORD_NAME_pat.search(line)
            if RECORD_NAME_search:
                vars = var_pat.findall(line)
                RECORD_NAME_value = vars[-1]
                if FIELDNAME_count.has_key(RECORD_NAME_value):
                    FIELD_NAME_num = FIELDNAME_count[RECORD_NAME_value]
                else: 
                    print "RECORD_NAME is not found!!!"
                    sys.exit()
                continue
                
            FIELD_NAME_search = FIELD_NAME_pat.search(line)
            if  FIELD_NAME_search:
                FIELD_NAME_num += 1
                if FIELD_NAME_num == 1: 
                    line = FIELD_NAME_search.group + "BEGIN" + "\n"
                else:
                    if FIELD_NEXT_FIELD:
                        line = FIELD_NAME_search.group + FIELD_NEXT_FIELD + "\n"
                    else:
                        print "FIELD_NEXT_FIELD is null!!!"
                        sys.exit()
    
#------------main func-------------------------------------
file = ""
if len(sys.argv) == 1:
    usage()
    sys.exit()
elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    usage()
    sys.exit()
else:
    file = sys.argv[1]

option = "-f"
if len(sys.argv) == 3:
    if sys.argv[2] == "-c" or sys.argv[2] == "--check":
        option = "-c"
    elif sys.argv[2] == "-f" or sys.argv[2] == "--fill":
        option = "-f"
        
    
file_list=[]
if os.path.isfile(file):
    file_list.append(file)
elif os.path.isdir(file):
    workPath=file
    for  root, dirs,files in os.walk(workPath):
        for file in files:
            if isDcdFile(file):
                file_list.append(root+"/"+file)
else:
    print "%s is not file or dir!!!"%(file)

for file in file_list:

    print "=====file:%s====="%(file)

    line_list = []
    READ_FILE   = open(file, "r")
    line = READ_FILE.readline()
    while(line):
        line_list.append(line)
        line = READ_FILE.readline()
    READ_FILE.close()
   
    FIELD_NAME_cout(line_list)
    
    check_FIELD_NAME(line_list)
                    

                 
                        
    
    