#! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import os
import sys
import re
import pdb
import subprocess
import string


def usage():
    print '''
    usage:
    getSpeed.py            : help info
    getSpeed.py -h         : help info
    getSpeed.py --help     : help info
    getSpeed.py filePreFix : filePreFix is prefix of stat file
    eg: getSpeed.py de_gprs_sgw_nokia
    
    '''

#2015-09-15 18:37:15.411545 de_ggprs_tap3_lte_2096.3567.1:/capes/xdr_file_op:Earlist="20150829061559" EndTim    e="2015-09-15 18:37:15.392357" ErrorStat="E1515:92624," FileStat="LTECNGO20150829CNT791.358:141767," Filter    Stat="F9000:2," Latest="20150829120337" NewTbcgCount="0" NoWriteCount="2" ReadFileName="LTECNGO20150829CNT7    91.358" ReadFileSize="38805655" ReadXdrCount="234393" Speed="2018" StartTime="2015-09-15 18:35:19.277156" S    umFee="0" WriteFailXdrCount="92624" WriteOkXdrCount="141767" ;
#2015-09-15 18:40:19.367732 de_ggprs_tap3_lte_2096.3567.1:/capes/xdr_file_op:Earlist="20150829101255" EndTim    e="2015-09-15 18:40:19.357280" ErrorStat="E1515:91188," FileStat="LTECNGO20150829CNT791.370:137621," Filter    Stat="F9000:2," Latest="20150829122733" NewTbcgCount="0" NoWriteCount="2" ReadFileName="LTECNGO20150829CNT7    91.370" ReadFileSize="38258758" ReadXdrCount="228811" Speed="5166" StartTime="2015-09-15 18:39:35.070113" S    umFee="0" WriteFailXdrCount="91188" WriteOkXdrCount="137621" ;
 
    
ReadXdrCount_pat = re.compile(r"ReadXdrCount=\"[0-9]+\"")
Speed_pat        = re.compile(r"Speed=\"[0-9]+\"")
data_pat         = re.compile(r"\d+")
date_pat         = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
shortLine_pat    = re.compile(r"\-")
time_pat         = re.compile(r"[0-9]{2}\:[0-9]{2}\:[0-9]{2}\.[0-9]{6}")
maoHao_pat       = re.compile(r"\:")

speedList = []
cdrnum    =500
minSpeed  = 0
def avgSpeedPerHourPerFile(file):
    READ_FILE   = open(file, "r")
    line = READ_FILE.readline()
    total = {}
    sum   = {}
    while(line):
        line = READ_FILE.readline()
        ReadXdrCount_search = ReadXdrCount_pat.search(line)
        Speed_search        = Speed_pat.search(line)
        if ReadXdrCount_search and Speed_search:
            ReadXdrCount = ReadXdrCount_search.group()
            Speed        = Speed_search.group()
            ReadXdrCount_data = data_pat.search(ReadXdrCount).group()
            ReadXdrCount_data = string.atoi(ReadXdrCount_data, 10)
            Speed_data        = data_pat.search(Speed).group()
            Speed_data        = string.atoi(Speed_data, 10)
        else:
            continue
            
        date_search = date_pat.search(line)
        time_search = time_pat.search(line)
        data=""
        time=""
        if date_search and time_search:
            date = date_search.group()
            date = shortLine_pat.sub("", date)
            time = time_search.group()
        else:
            continue
        #pdb.set_trace()
        if ReadXdrCount_data > cdrnum:
            tag=date+time[0:2]  #$1substr($2,1,2);
            if total.has_key(tag):
                total[tag]=total[tag]+ReadXdrCount_data;
            else:
                total[tag] = ReadXdrCount_data
            if sum.has_key(tag):
                sum[tag]=sum[tag]+ReadXdrCount_data*Speed_data;
            else:
                sum[tag]=ReadXdrCount_data*Speed_data;
    READ_FILE.close()
    
    #pdb.set_trace()
    #print "\nxdr size > %s :"%(cdrnum);
    print "\nfile: %s"%(file)
    for key in total.keys():
        print "Date: %s-%s-%s %s"%(key[0:4],key[4:6],key[6:8],key[8:10])
        print "xdr size:%d"%(total[key])
        #printf(">%d条记录文件个数:%d，<=%d条记录文件个数:%d\n", cdrnum, fileNum1[a_total[i]], cdrnum, fileNum2[a_>
        avgSpeed = sum[key]/total[key]
        print "speed:%.2f"%(avgSpeed)
        
        global minSpeed
        if minSpeed == 0:
            minSpeed = avgSpeed
        elif minSpeed > avgSpeed:
            minSpeed = avgSpeed
        
#-----------统计--------------------------------------
#分类统计

filePreFix = ""
if len(sys.argv) == 1:
    usage()
    sys.exit()
elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    usage()
    sys.exit()
else:
    filePreFix = sys.argv[1]

file_list = []
workPath = "./"
filePreFix_pat = re.compile("%s"%(filePreFix))
for  root, dirs,files in os.walk(workPath):
    for file in files:
        if filePreFix_pat.search(file):
            file_list.append(file)

#pdb.set_trace()                  
for file in file_list:
    avgSpeedPerHourPerFile(file)

print
print
print "====the minimum speed===="
print "%d"%(minSpeed)
