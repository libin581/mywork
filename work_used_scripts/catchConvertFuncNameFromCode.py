#! /usr/bin/python

import os
import sys
import re
import pdb


def catchConvertFuncName(sourceFilePath):
    #sourceFilePath="/home/ut/work/openbilling60_cmcc/rating_billing/rating/decode/tuning/Ng/"
    convertFuncNameList=[]

    header_file_pat=re.compile(r".*\.h|.*\.hpp")
    func_pat=re.compile(r"\w+\s+\w+\(.+\);")
    func_name_pat=re.compile(r"\w+\(")
    for  root, dirs,files in os.walk(sourceFilePath):
        for file in files:
            if not header_file_pat.search(file):
               continue

            header_file= open(root+file, "r")
            line = header_file.readline()
            while(line):
                func_search=func_pat.search(line)
                if func_search:
                    func_name_search=func_name_pat.search(line)
                    (start,end)=func_name_search.span()
                    func_name=line[start:end-1]
                    convertFuncNameList.append(func_name)
                line = header_file.readline()
            header_file.close()

    convert_func_statistic= open("convert_func_statistic", "w")
    for func in convertFuncNameList:
        convert_func_statistic.write("%s\n" % (func))
    convert_func_statistic.close()
    return convertFuncNameList