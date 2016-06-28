#! /usr/bin/python

import os
import shutil
import sys
import re
import pdb

dupCheckProcess=(
"1005", "1006", "1066", "1067", "1069", 
"1070", "1071", "1077", "1078", "1079", 
"1081", "1082", "1085", "1086", "1091", 
"1092", "1093", "1094", "1134", "1146", 
"1147", "1148", "1149", "1150", "1152", 
"1156", "1157", "1160", "1163", "1164", 
"1166", "1168", "1169", "1201", "1203", 
"1208", "1211", "1212", "1215", "1217", 
"1221", "1222", "1223", "1224", "1225", 
"1226", "1227", "1228", "1230", "1231", 
"1232", "1234", "1235", "1236", "1237", 
"1238", "1240", "1241", "1242", "1243", 
"1244", "1246", "1247", "1249", "1301", 
"1306", "1404", "1501", "1508", "1509", 
"1510", "1511", "1512", "1514", "1607", 
"1608", "1609", "1611", "1612", "1618", 
"1619", "1620", "1627", "1628", "1629", 
"1630", "1631", "1632", "1638", "1639", 
"1640", "1641", "1665", "1667",
);

serviceType=(
"gsm","sms","ggprs","ismg","gprs","addvalue",
"wlan","java","mms","vc","ch","stm","wap"
)

workpath="/home/ut/work/testIssue/jx/dupcheck_data/"
      
recordTable=[]
cfgfile_pat=re.compile(r"\.cfg")
for  root, dirs, files in os.walk(workpath):
    print "[%s]:"%(root)
    for file in files:
        #check is dupcheck process
        #processFound=False
        #for process in dupCheckProcess:
        #    process_pat=re.compile(r"%s"%(process))
        #    if process_pat.search(file):
        #        processFound=True
        #        break

        #if processFound==False:
        #    continue
        
        if not cfgfile_pat.search(file):
            continue

        filepath=root+"/"+file
        ORIG_FILE= open(filepath, "r")
        line = ORIG_FILE.readline()
        keywordfound=0
        HashSource_pat=re.compile(r"\[HashSource")
        decode_pat=re.compile(r"\[decode")
        comment_pat=re.compile(r"^#|^\s+#")
        blank_pat=re.compile(r"^$")
        space_enter_pat=re.compile(r"\s+\n$|\n$")
        processEnd_pat=re.compile(r"\[.+\]")
        decodeProcessStart=False
        dupCheckProcessStart=False
        hashTable={}
        hashTable_another={}
        hashTable["filename"]=file
        hashTable_another["filename"]=file
        Dupkind_pat=re.compile(r"DupKind\s*=\s*0")
        while line:
            #skip comments lines and blank lines
            if comment_pat.search(line) or blank_pat.search(line):
                line = ORIG_FILE.readline()
                continue

            if Dupkind_pat.search(line):
                line = ORIG_FILE.readline()
                break
                
            if decodeProcessStart==True or dupCheckProcessStart==True:
                if processEnd_pat.search(line):
                    decodeProcessStart=False
                    dupCheckProcessStart=False

            if decodeProcessStart==False and dupCheckProcessStart==False:
                if decode_pat.search(line):
                    #pdb.set_trace()
                    decodeProcessStart=True

                if HashSource_pat.search(line):
                    dupCheckProcessStart=True
                    keywordfound+=1

                line = ORIG_FILE.readline()
                continue

            if decodeProcessStart==True and dupCheckProcessStart==True:
                print "decodeProcessStart=True,dupCheckProcessStart=True"
                sys.exit()

            #remove space and newline
            space_enter_search=space_enter_pat.search(line)
            if space_enter_search:
                line=space_enter_pat.sub("",line)

            if decodeProcessStart==True:
                template_pat=re.compile(r"/template/")
                template_search=template_pat.search(line)
                #pdb.set_trace()
                if template_search:
                    #pdb.set_trace()
                    idx=template_search.end()
                    hashTable["decodeTemplate"]=line[idx:]
                    hashTable_another["decodeTemplate"]=line[idx:]

            if dupCheckProcessStart==True:
                #pdb.set_trace()
                equal_pat=re.compile(r"=")
                equal_search=equal_pat.search(line)
                if equal_search:
                    (startIdx,endIdx)=equal_search.span()
                    field_name=line[:startIdx]
                    field_value=line[endIdx:]
                    if keywordfound>1:
                        if hashTable_another.has_key(field_name):
                            hashTable_another[field_name]+="----"+field_value
                        else:
                            hashTable_another[field_name]=field_value
                    else:
                        if hashTable.has_key(field_name):
                            hashTable[field_name]+="----"+field_value
                        else:
                            hashTable[field_name]=field_value

            line = ORIG_FILE.readline()
            continue
            #end of line

        if keywordfound==0:
            print "%s has no key word!!!"%(file)

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
        print "%s:%-40s"%("filename",record["filename"]),
        #del record["filename"]

    if record.has_key("decodeTemplate"):
        print "%s:%-25s"%("decodeTemplate",record["decodeTemplate"]),
        #del record["decodeTemplate"]

    if record.has_key("Combination"):
        print "%s:%-70s"%("Combination",record["Combination"]),
        #del record["Combination"]

    if record.has_key("FieldName"):
        print "%s:%-15s"%("FieldName",record["FieldName"]),
        #del record["FieldName"]

    if record.has_key("Value"):
        print "%s:%-s"%("Value",record["Value"]),
        #del record["Value"]

    if record.has_key("SwapInterval"):
        print "%s:%-s"%("SwapInterval",record["SwapInterval"]),
    
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
