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
        lineChange=0
        newLines = []
        WRITE_FILE = open('./new/'+file,'w')
        READ_FILE  = open('./old/'+file,'r')
        line = READ_FILE.readline()
        while line:
            #pdb.set_trace()
            callType = int(line[0:2])
            feeType  = int(line[122:123])
            duration = int(line[70:76])
            cFee     = int(line[123:129])
            #print "callType:%d,feeType:%d,duration:%d,cFee:%d"%(callType, feeType, duration, cFee)
            if (callType == 3) and \
                (feeType == 1) and ( not cFee == 0):
                cFee = (duration+59)/60*100
                cFee = str(int(cFee))
                cFee = '0'*(6-len(cFee))+cFee
                
                line = line[0:123]+cFee+line[129:]
                lineChange += 1
                
            WRITE_FILE.write(line)
            line = READ_FILE.readline()
                    
        WRITE_FILE.close()
        READ_FILE.close()
        
        #print "file %s change line number %d"%(file, lineChange)