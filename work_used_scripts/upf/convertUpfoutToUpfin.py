#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import pdb

if not os.path.exists('./new'):
    os.makedirs('./new')

for  root, dirs,files in os.walk('./old'):
    for file in files:
        print "======================"
        print "process file:%s"%(file)

        WRITE_FILE = open('./new/'+file,'w')
        READ_FILE  = open('./old/'+file,'r')
        line = READ_FILE.readline()
        while line:
            #pdb.set_trace()
            callType = int(line[0:2])
            if callType == 10 or callType == 90:
                line = READ_FILE.readline()
                continue
            
            duration = int(line[70:76])
            startTime = line[56:70]
            cFee     = int(line[123:129])
            LFee1    = int(line[129:137])
            LFee2    = int(line[143:151])
            
            if callType == 3 and int(startTime[4:]) < 906000000:
                line = READ_FILE.readline()
                continue
            
            #print "callType:%d,feeType:%d,duration:%d,cFee:%d"%(callType, feeType, duration, cFee)
            billFlag = 0
            if (callType == 1):
                billFlag = 0
            elif callType == 2:
                billFlag = 1
            elif callType == 3:
                billFlag = 2
            else:
                print "error callType value"
               
                
            newline = line[0:247]
            newline += ';D;0;0;0;'+str(duration)+';'+startTime+';'
            newline += '0;'+str(cFee)+';'+str(LFee1)+';'+str(LFee2)+';'+str(billFlag)+';'
            newline += '0;0;'
                
            line = READ_FILE.readline()
            #print line
            callType = line[0:2]
            if not callType == '90':
                newline += '\n'
            
            WRITE_FILE.write(newline)
                    
        WRITE_FILE.close()
        READ_FILE.close()
        
#for  root, dirs,files in os.walk('./new'):
#    for file in files:
#        os.system("grep -v '^$' %s > %s"%('./new/'+file,'./new/'+file[0:-1]))