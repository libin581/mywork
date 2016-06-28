#! /usr/bin/python

import sys
import os
import re
import shutil
import subprocess
import pdb

convert_common_cpp="/home/libin3/CMCC_ZJ/billing/openbilling60_cmcc/rating_billing/\
rating/decode/tuning/ng/convert_common.cpp"

convert_jx_cpp="/home/libin3/CMCC_ZJ/billing/openbilling60_cmcc/rating_billing/\
rating/decode/tuning/ng/convert_jx.cpp"

convert_nm_cpp="/home/libin3/CMCC_ZJ/billing/openbilling60_cmcc/rating_billing/\
rating/decode/tuning/ng/convert_nm.cpp"

convert_xz_cpp="/home/libin3/CMCC_ZJ/billing/openbilling60_cmcc/rating_billing/\
rating/decode/tuning/ng/convert_xz.cpp"

convert_common_func_set=[]
convert_nm_func_set=[]
convert_jx_func_set=[]
convert_xz_func_set=[]


def getConvertFuncSet(file,funcSet):
    func_pat=re.compile(r"\w+\s+\w+\(\s*CXdr&")
    func_name_pat=re.compile(r"\w+\(")
    xdrField_pat=re.compile(r"CXdrField.+\"[A-Z_]+\"")
    xdrField_name_pat=re.compile(r"\"[A-Z_]+\"")

    ORIG_FILE= open(file, "r")
    line = ORIG_FILE.readline()
    func_info={}
    func_info["field"]=""
    while(line):
        func_pat_search=func_pat.search(line)
        if func_pat_search:
            if func_info.has_key("funcName"):
                #pdb.set_trace()
                funcSet.append(func_info)
                func_info={}
                func_info["field"]=""
            func_name_search = func_name_pat.search(line)
            if func_name_search:
                (stIdx,endIdx)=func_name_search.span()
                func_info["funcName"]=line[stIdx:endIdx-1]
        else:
            if xdrField_pat.search(line):
                xdrField_name_search=xdrField_name_pat.search(line)
                if xdrField_name_search:
                    (stIdx,endIdx)=xdrField_name_search.span()
                    func_info["field"]+="{" + line[stIdx:endIdx] + "}"
                    
        line = ORIG_FILE.readline()
    ORIG_FILE.close()    

getConvertFuncSet(convert_common_cpp,convert_common_func_set)
getConvertFuncSet(convert_nm_cpp,convert_nm_func_set)
getConvertFuncSet(convert_xz_cpp,convert_xz_func_set)
getConvertFuncSet(convert_jx_cpp,convert_jx_func_set)


def queryFuncSet(funcSet, field):
    field_pat=re.compile(r"{\"%s\"}"%(field))
    for func in funcSet:
        if field_pat.search(func["field"]):
            print"%s"%(func["funcName"])

def printHelp():
    print "2 or 3 parameters are needed: field name, province, decode template"
    print "eg1: field2Convertfunc.py DR_TYPE nm d_gsm.dcd"
    print "eg2: field2Convertfunc.py DR_TYPE nm"
    print 
            
decodeTemp = None
            
if len(sys.argv) <= 1:
    printHelp()
    sys.exit()
elif len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
    printHelp()  
    sys.exit()
elif len(sys.argv) == 3:
    province=sys.argv.pop()
    fieldName=sys.argv.pop()
elif len(sys.argv) == 4:
    decodeTemp=sys.argv.pop()
    province=sys.argv.pop()
    fieldName=sys.argv.pop()
else:
    print "not enough input parameters are needed!!!"
    sys.exit()
    
print
print "fieldName=%s, province=%s, decodeTemp=%s"%(fieldName, province, decodeTemp)
print
    
print "following functions relate with %s"%(fieldName)
splitSymbol="---"
print "\n%sfile:convert_common.cpp%s"%(splitSymbol,splitSymbol)
queryFuncSet(convert_common_func_set, fieldName)

if province == "neimeng" or province == "nm":
    tempPath="/home/libin3/CMCC_ZJ/billing/openbilling60_cmcc/rating_billing/rating/decode/template/nm/"
    print "\n%sfile:convert_nm.cpp%s"%(splitSymbol,splitSymbol)
    queryFuncSet(convert_nm_func_set, fieldName)
elif province == "xizang" or province == "xz":
    tempPath="/home/libin3/CMCC_ZJ/billing/openbilling60_cmcc/rating_billing/rating/decode/template/xz/"
    print "\n%sfile:convert_xz.cpp%s"%(splitSymbol,splitSymbol)
    queryFuncSet(convert_xz_func_set, fieldName)
elif province == "jiangxi" or province == "jx":
    tempPath="/home/libin3/CMCC_ZJ/billing/openbilling60_cmcc/rating_billing/rating/decode/template/jx/"
    print "\n%sfile:convert_jx.cpp%s"%(splitSymbol,splitSymbol)
    queryFuncSet(convert_jx_func_set, fieldName)
else:
    print "unknow provinve %s"%(province)

    
def queryFuncSet2(funcSet, funcName, field):
    field_pat=re.compile(r"{\"%s\"}"%(field))
    for func in funcSet:
        if func["funcName"] == funcName:
            if field_pat.search(func["field"]):
                print"%s"%(func["funcName"])
    
    
tempPublic="/home/libin3/CMCC_ZJ/billing/openbilling60_cmcc/rating_billing/rating/decode/template/public/"
if decodeTemp is not None:
    docodeTemp1=tempPath+decodeTemp
    decodeTemp2=tempPublic+decodeTemp
    if os.path.exists(docodeTemp1):
        ORIG_FILE=open(docodeTemp1, 'r')
    elif os.path.exists(decodeTemp2):
        ORIG_FILE=open(decodeTemp2, 'r')
    else:
        print "can't found %s!!!"%(decodeTemp)

    convert_func=[]
    RECORD_CONVERT_FUNC_pat=re.compile(r"RECORD_CONVERT_FUNC")
    func_name_pat=re.compile(r"[a-zA-Z0-9]+")
    line = ORIG_FILE.readline()
    while(line):
        RECORD_CONVERT_FUNC_search=RECORD_CONVERT_FUNC_pat.search(line)
        if RECORD_CONVERT_FUNC_search:
            endIdx=RECORD_CONVERT_FUNC_search.end()
            temp=line[endIdx+1:]
            func_name_search=func_name_pat.search(temp)
            if func_name_search:
                convert_func.append(func_name_search.group())
        line = ORIG_FILE.readline()
    ORIG_FILE.close()   

    print
    print "==============================================="
    print "following function in template relate with %s"%(fieldName)
    print
    splitSymbol="---"
    for func in convert_func:
        #print "\n%sfile:convert_common.cpp%s"%(splitSymbol,splitSymbol)
        queryFuncSet2(convert_common_func_set, func, fieldName)
    
        if province == "neimeng" or province == "nm":
         #   print "\n%sfile:convert_nm.cpp%s"%(splitSymbol,splitSymbol)
            queryFuncSet2(convert_nm_func_set, func, fieldName)
        elif province == "xizang" or province == "xz":
          #  print "\n%sfile:convert_xz.cpp%s"%(splitSymbol,splitSymbol)
            queryFuncSet2(convert_xz_func_set, func, fieldName)
        elif province == "jiangxi" or province == "jx":
           # print "\n%sfile:convert_jx.cpp%s"%(splitSymbol,splitSymbol)
            queryFuncSet2(convert_jx_func_set, func, fieldName)

