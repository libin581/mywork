#! /usr/bin/python

import subprocess
import os
import shutil
import sys
import re
import pdb

serviceType=(
"gsm","sms","ggprs","ismg","gprs","addvalue",
"wlan","java","mms","vc","ch","stm","wap"
)

workpath="/home/ut/work/testIssue/nm/dupcheck/dupcheck_cfg/"
#workpath=workpath+"dupcheck/"
      
recordTable=[]
for  root, dirs, files in os.walk(workpath):
    print "[%s]:"%(root)
    for file in files:
        filepath=root+"/"+file
        ORIG_FILE= open(filepath, "r")
        line = ORIG_FILE.readline()
        keywordfound=0
        keyword_pat=re.compile(r"<HashSource>")
        keyword_end_pat=re.compile(r"</HashSource>")
        comment_start_pat=re.compile(r"<!--")
        comment_end_pat=re.compile(r"-->")
        processStart=False
        commentStart=False
        service_number=0
        hashTable={}
        hashTable_another={}
        hashTable["filename"]=file
        hashTable_another["filename"]=file
        while line:
            if comment_start_pat.search(line):
                commentStart=True

            if comment_end_pat.search(line):
                commentStart=False
                line = ORIG_FILE.readline()
                continue

            if commentStart==True:
                line = ORIG_FILE.readline()
                continue

            if processStart==False:
                if keyword_pat.search(line):
                    keywordfound+=1
                    processStart=True
                line = ORIG_FILE.readline()
                continue
            
            if keyword_end_pat.search(line):
                processStart=False
                line = ORIG_FILE.readline()
                continue

            field_name_pat     = re.compile(r"\s+<\w+>")
            field_name_search  = field_name_pat.search(line)
            if field_name_search:
                field_name=field_name_search.group()
                rm_pat=re.compile(r".+<|>")
                rm_search=rm_pat.search(field_name)
                if rm_search:
                    field_name=rm_pat.sub("",field_name)

            field_value_pat    = re.compile(r">.+</")
            field_value_search = field_value_pat.search(line)
            if field_value_search:
                field_value=field_value_search.group()
                rm_pat=re.compile(r">")
                rm_search=rm_pat.search(field_value)
                if rm_search:
                    field_value=rm_pat.sub("",field_value)
                rm_pat=re.compile(r"</")
                rm_search=rm_pat.search(field_value)
                if rm_search:
                    field_value=rm_pat.sub("",field_value)

                    
                    
            if field_value_search and field_name_search:
                service_number+=1

            if service_number==1:
                if field_value_search:
                    if hashTable.has_key(field_name):
                        field_value_pat=re.compile(field_value)
                        if not field_value_pat.search(hashTable[field_name]):
                            hashTable[field_name]+="----"+field_value
                    else:
                        hashTable[field_name]=field_value
                elif field_name_search:
                    #pdb.set_trace()  
                    if hashTable.has_key("fieldname"):
                        field_value_pat=re.compile(field_name)
                        if not field_value_pat.search(hashTable["fieldname"]):
                            hashTable["fieldname"]+="----"+field_name
                    else:
                        hashTable["fieldname"]=field_name
            else:
                if field_value_search:
                    if hashTable_another.has_key(field_name):
                        field_value_pat=re.compile(field_value)
                        if not field_value_pat.search(hashTable_another[field_name]):
                            hashTable_another[field_name]+="----"+field_value
                    else:
                        hashTable_another[field_name]=field_value
                elif field_name_search:
                    #pdb.set_trace()  
                    if hashTable_another.has_key("fieldname"):
                        field_value_pat=re.compile(field_name)
                        if not field_value_pat.search(hashTable_another["fieldname"]):
                            hashTable_another["fieldname"]+="----"+field_name
                    else:
                        hashTable_another["fieldname"]=field_name

            line = ORIG_FILE.readline()
            #end of line

        if keywordfound==0:
            print "%s has no key word!!!"%(file)
        elif keywordfound>1:
            print "%s has more than one key word"%(file)


        if len(hashTable)>2:
            recordTable.append(hashTable)
        if len(hashTable_another)>2:
            recordTable.append(hashTable_another)
        #end of file

def printRecord(record):
#    field_name_list=("filename","decodeTemplate","SwapInterval",
#    "WindowSize","Combination","TimeStamp","Arithmetic","RollBack",
#    "ExclusiveKey")

    if record.has_key("filename"):
        print "%s:%-50s"%("filename",record["filename"]),
        del record["filename"]

    if record.has_key("decodeTemplate"):
        print "%s:%-20s"%("decodeTemplate",record["decodeTemplate"]),
        del record["decodeTemplate"]

    if record.has_key("Combination"):
        print "%s:%-80s"%("Combination",record["Combination"]),
        del record["Combination"]

    if record.has_key("DrType"):
        print "%s:%-20s"%("DrType",record["DrType"]),
        del record["DrType"]

    if record.has_key("FieldName"):
        print "%s:%-50s"%("FieldName",record["FieldName"]),
        del record["FieldName"]

    if record.has_key("Value"):
        print "%s:%-80s"%("Value",record["Value"]),
        del record["Value"]

    if record.has_key("SwapInterval"):
        print "%s:%-80s"%("SwapInterval",record["SwapInterval"]),
        del record["SwapInterval"]

        
    #for key in record.keys():
    #    print"%s:%s    "%(key,record[key]),
    print " "

#pdb.set_trace()
print "===================================="
print "%d recrod"%(len(recordTable))

for service in serviceType:
    print "[%s]:"%(service)
    service_pat=re.compile(r"%s"%(service))
    for record in recordTable:
        if not record.has_key("printFlag"):
            if service_pat.search(record["filename"]):
                printRecord(record)
                record["printFlag"]=True

print "[others]:"
for record in recordTable:
    if not record.has_key("printFlag"):
        printRecord(record)
