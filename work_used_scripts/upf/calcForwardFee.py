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
        lastLine = []
        forwardBasicFee = 0
        while line:
            #pdb.set_trace()
            callType = int(line[0:2])
            cFee = 0
            if not (callType == 10 or callType == 90):
                cFee     = int(line[123:129])
            if callType == 3:
                forwardBasicFee += cFee
                
            if not callType == 90:
                WRITE_FILE.write(line)
            else:
                lastLine = line
            line = READ_FILE.readline()
    
        READ_FILE.close()
        
        forwardBasicFee = (forwardBasicFee + 5)/10
        print "forwardBasicFee=%d"%(forwardBasicFee)
        
        WRITE_FILE.close()