#! /usr/bin/python
# -*- coding: utf-8 -*-
# 目前该脚本只能检查，不能自动完成filed name的编号
# asn1格式不能检查

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
    decode_dcd_fieldname_fill.py -c *.dcd   : check decode template
    decode_dcd_fieldname_fill.py -f *.dcd   : audo fill decode template
    decode_dcd_fieldname_fill.py path       : check and fill all decode templates at this path
    
    eg: 
       1. decode_dcd_fieldname_fill.py -c file.dcd
       2. decode_dcd_fieldname_fill.py -f file.dcd
       3. decode_dcd_fieldname_fill.py -c ./ 
    
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
    
blank_line_pat = re.compile(r"^\s*$")
def skipBlankLine(line):
    if blank_line_pat.search(line):
        return True
    else:
        return False
    
comment_pat = re.compile(r"\/\/")
def removeComment(line):
    if comment_pat.search(line):
        #pdb.set_trace()
        (s,e)=comment_pat.search(line).span()
        line = line[:s]
    return line
    
def removeChangeLine(line):
    line = line.replace("\r\n","")
    line = line.replace("\n","")
    return line
    
#define 正则表达式
RECORD_pat        = re.compile(r"^RECORD$") #    RECORD
FIELD_pat         = re.compile(r"^FIELD$") # FIELD
FIELD_NAME_pat    = re.compile(r"^FIELD_NAME\s*=\s*\w+$") #            FIELD_NAME = BEGIN
FIELD_NEXT_FIELD_pat = re.compile(r"^FIELD_NEXT_FIELD\s*=\s*\w+$") #            FIELD_NEXT_FIELD =
FIELD_LEAF_pat    = re.compile(r"^FIELD_LEAF\s*=\s*YES$|^FIELD_LEAF\s*=\s*NO$")
DECODE_pat        = re.compile(r"^DECODE$")
left_bracket_pat  = re.compile(r"^{")  # {
right_bracket_pat = re.compile(r"^}")  # {
RECORD_NAME_pat   = re.compile(r"^RECORD_NAME\s*=\s*\w+$") #          RECORD_NAME = control
RECORD_TYPE_pat   = re.compile(r"^RECORD_TYPE\s*=\s*\w+$")
ASN_BER_pat           = re.compile(r"ASN|PROPERTY_FILE_ENCODE_TYPE\s*=\s*BER")
ENCODE_TYPE_pat   = re.compile(r"PROPERTY_FILE_ENCODE_TYPE\s*=\s*\w+$")
var_pat = re.compile(r"\w+")

isInRecord      = False
bracket_deep      = 0
fieldNameCount  = 0
RECORD_NAME = ""
RECORD_TYPE = ""
FIELD_NAME = ""
FIELD_NEXT_FIELD = ""
def recordVarsInit():
    global isInRecord 
    global bracket_deep
    global fieldNameCount
    global RECORD_NAME
    global RECORD_TYPE
    global FIELD_NAME
    global FIELD_NEXT_FIELD
    isInRecord       = False
    bracket_deep     = 0
    fieldNameCount   = 0
    RECORD_NAME      = ""
    RECORD_TYPE      = ""
    FIELD_NAME       = ""
    FIELD_NEXT_FIELD = ""

isInField    = False
hasFieldLeaf = False
hasFieldName = False
hasFieldNextField = False
hasDecode    = False
def fieldVarsInit():
    global isInField
    global hasFieldLeaf
    global hasFieldName
    global hasFieldNextField
    global hasDecode
    isInField    = False
    hasFieldLeaf = False
    hasFieldName = False
    hasFieldNextField = False
    hasDecode    = False


def checkField(lines):
    global isInRecord 
    global bracket_deep
    global fieldNameCount
    global RECORD_NAME
    global FIELD_NAME
    global RECORD_TYPE
    global FIELD_NEXT_FIELD
    global isInField
    global hasFieldLeaf
    global hasFieldName
    global hasFieldNextField
    global hasDecode

    recordVarsInit()
    fieldVarsInit()
    encodeType = ""
    for i, line in enumerate(lines):
        i+=1
        line = removeComment(line)
        line = removeChangeLine(line)
        line = line.strip()
        #pdb.set_trace()
        if skipBlankLine(line) == True:
            continue
           
        if not encodeType:
            if ENCODE_TYPE_pat.search(line):
                #pdb.set_trace()
                vars = line.split("=")
                encodeType = vars[-1].strip()
        else:
            if not encodeType == "ASCII":
                print "file is not ASC encode"
                break;
           
        if isInRecord == False:
            if RECORD_pat.search(line):
                isInRecord = True
            continue
        else:
            if left_bracket_pat.search(line):
                bracket_deep += 1

            if right_bracket_pat.search(line):
                bracket_deep -= 1
                
            if bracket_deep == 0: #the end of record
                #pdb.set_trace()
                if RECORD_NAME:
                    print "RECORD_NAME:%s, count:%d"%(RECORD_NAME, fieldNameCount)
                    print
                else:
                    print "line: %d RECORD_NAME is null!!!"%(i)
                    sys.exit()
                if not RECORD_TYPE:
                    print "line: %d RECORD_TYPE is null!!!"%(i)
                    #sys.exit()
                if not (RECORD_TYPE == "TAIL" or RECORD_TYPE == "HEAD") and not FIELD_NEXT_FIELD == "NULL":
                    print "line %d, the last FIELD_NEXT_FIELD is not NULL"%(i)
                    sys.exit()
                    
                recordVarsInit()
                fieldVarsInit()
            elif bracket_deep == 1:
                if not RECORD_NAME:
                    RECORD_NAME_search = RECORD_NAME_pat.search(line)
                    if RECORD_NAME_search:
                        vars = var_pat.findall(line)
                        RECORD_NAME = vars[-1]
                if not RECORD_TYPE:
                    RECORD_TYPE_search = RECORD_TYPE_pat.search(line)
                    if RECORD_TYPE_search:
                        vars = var_pat.findall(line)
                        RECORD_TYPE = vars[-1]
                if isInField == True:
                    if hasFieldName == False:
                        print "line %d has not correct FIELD_NAME"%(i)
                        sys.exit()
                    if hasFieldNextField == False:
                        print "line %d has not correct FIELD_NEXT_FIELD"%(i)
                        sys.exit()
                    if hasFieldLeaf == False:
                        print "line %d has not correct FIELD_LEAF"%(i)
                    if hasDecode == False:
                        print "line %d has not correct DECODE"%(i)
                        sys.exit()
                    if fieldNameCount == 1:
                        if not FIELD_NAME == "BEGIN":
                            print "line %s, the first FIELD_NAME must be 'BEGIN' "%(i)
                            sys.exit()
                    fieldVarsInit()
            elif bracket_deep == 2:
                isInField = True
                FIELD_NAME_search = FIELD_NAME_pat.search(line)
                if  FIELD_NAME_search:
                    fieldNameCount += 1
                    hasFieldName = True
                    vars = var_pat.findall(line)
                    FIELD_NAME = vars[-1]
                    if not FIELD_NAME == "BEGIN":
                        if not FIELD_NEXT_FIELD and not FIELD_NAME == FIELD_NEXT_FIELD:
                            print "line %d FIELD_NAME is not right"%(i)
                            sys.exit()
                FIELD_LEAF_search = FIELD_LEAF_pat.search(line)
                #pdb.set_trace()
                if FIELD_LEAF_search:
                    #pdb.set_trace()
                    hasFieldLeaf = True
                FIELD_NEXT_FIELD_search = FIELD_NEXT_FIELD_pat.search(line)
                if FIELD_NEXT_FIELD_search:
                    hasFieldNextField = True
                    vars = var_pat.findall(line)
                    FIELD_NEXT_FIELD = vars[-1]
                DECODE_search = DECODE_pat.search(line)
                if DECODE_search:
                    hasDecode = True
            elif bracket_deep < 0:
                print "right bracket is more than left bracket"
                sys.exit()
    
#fill all FIELD_NAME and FIELD_NEXT_FIELD
def fillField(lines):
    isInRecord      = False
    bracket_deep      = 0
    fieldNameCount    = 0
    FIELD_NEXT_FIELD = []
    for i, line in enumerate(lines):
        if skipCommentLine(line) == True:
            continue
           
        if isInRecord == False:
            if RECORD_pat.search(line):
                isInRecord = True
            continue
        else:
            if left_bracket_pat.search(line):
                bracket_deep += 1
                continue
            if right_bracket_pat.search(line):
                bracket_deep -= 1
                if bracket_deep == 0:
                    isInRecord = False
                continue
                
            RECORD_NAME_search = RECORD_NAME_pat.search(line)
            if RECORD_NAME_search:
                vars = var_pat.findall(line)
                RECORD_NAME_value = vars[-1]
                if FIELDNAME_count.has_key(RECORD_NAME_value):
                    fieldNameCount = FIELDNAME_count[RECORD_NAME_value]
                else: 
                    print "RECORD_NAME is not found!!!"
                    sys.exit()
                continue
                
            FIELD_NAME_search = FIELD_NAME_pat.search(line)
            if  FIELD_NAME_search:
                fieldNameCount += 1
                if fieldNameCount == 1: 
                    line = FIELD_NAME_search.group + "BEGIN" + "\n"
                else:
                    if FIELD_NEXT_FIELD:
                        line = FIELD_NAME_search.group + FIELD_NEXT_FIELD + "\n"
                    else:
                        print "FIELD_NEXT_FIELD is null!!!"
                        sys.exit()
    
#------------main func-------------------------------------
def main():
    file = ""
    if len(sys.argv) == 1:
        usage()
        sys.exit()
    elif len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        usage()
        sys.exit()
    elif len(sys.argv) == 3 :
        file = sys.argv[2]
    else:
        print "error input parameters"
        usage()

    option = ""
    if len(sys.argv) == 3:
        if sys.argv[1] == "-c" or sys.argv[1] == "--check":
            option = "-c"
        elif sys.argv[1] == "-f" or sys.argv[1] == "--fill":
            option = "-f"
            
        
    file_list=[]
    if os.path.isfile(file):
        file_list.append(file)
    elif os.path.isdir(file):
        workPath=file
        for  root, dirs,files in os.walk(workPath):
            for file in files:
                if isDcdFile(file):
                    file_list.append(root+file)
    else:
        print "%s is not file or dir!!!"%(file)

    for file in file_list:

        print "=====file:%s====="%(file)

        READ_FILE   = open(file, "r")
        lines = READ_FILE.readlines()
        READ_FILE.close()
       
        if option == "-c":
            #pdb.set_trace()
            checkField(lines)
                    
if __name__ == '__main__':
    main()
                 
                        
    
    
