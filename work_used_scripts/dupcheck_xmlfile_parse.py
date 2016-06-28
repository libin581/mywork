#! /usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import os
import shutil
import sys
import re
import pdb
from xml.etree import ElementTree

workpath="/home/ut/work/testIssue/nm/dupcheck/dupcheck_cfg/"

file_servicetype_table={}
    
fileType_pat=re.compile(r"\.xml")
for  root, dirs, files in os.walk(workpath):
    for file in files:
        if not fileType_pat.search(file):
            continue
    
        serviceType_pat=re.compile(r"<DrType>.+</DrType>")
        DrType_pat = re.compile(r"dr_[a-z]+")
        service=None
        ORIG_FILE= open(root+'/'+file, "r")
        line = ORIG_FILE.readline()
        while line:
            serviceType_search = serviceType_pat.search(line)
            if serviceType_search:
                DrType_search = DrType_pat.search(line)
                if DrType_search:
                    service = DrType_search.group()
                    break
            else:
                line = ORIG_FILE.readline()
                
        ORIG_FILE.close()
                
        if service == None:
            if file_servicetype_table.has_key("others"):
                file_servicetype_table["others"].append(root+'/'+file)
            else:
                file_servicetype_table["others"]=[]
                file_servicetype_table["others"].append(root+'/'+file)
        else:
            #pdb.set_trace()
            if file_servicetype_table.has_key(service):
                file_servicetype_table[service].append(root+'/'+file)
            else:
                file_servicetype_table[service]=[]
                file_servicetype_table[service].append(root+'/'+file)
                
                
print "======================xml file dupcheck list======================"
print
for service in file_servicetype_table.keys():
    print "**********************************************************"
    print "************    %s    ************"%(service)
    print "**********************************************************"
    for file in file_servicetype_table[service]:
        print
        print "filename: %s"%(file)
        
        pdb.set_trace()
        root = ElementTree.parse(r"%s"%(file))
        for oneflows in root.findall('flows'):
            for flow in oneflows.getchildren():
                for oneNodes in flow.findall('nodes'):
                    for node in oneNodes.getchildren():
                        for node_configs in node.findall('node_configs'):
                            #pdb.set_trace()
                            for HashSource in node_configs.findall('HashSource'):
                                #pdb.set_trace()
                                subElemNum=0
                                for subElem in HashSource.getchildren():
                                    subElemNum = subElemNum+1
                                    DrType      = subElem.find("DrType")
                                    Combination = subElem.find("Combination")
                                    FieldName   = subElem.find("FieldName")
                                    Value       = subElem.find("Value")
                                    SwapInterval= subElem.find("SwapInterval")
                                    print "[%s]"%(subElemNum)
                                    if DrType is not None:
                                        print "DrType:%s"%(DrType.text)
                                    if Combination is not None:
                                        print "Combination:%s"%(Combination.text)
                                    if FieldName is not None:
                                        print "FieldName:%s"%(FieldName.text)
                                    if Value is not None:
                                        print "Value:%s"%(Value.text)
                                    if SwapInterval is not None:
                                        print "SwapInterval:%s"%(SwapInterval.text)
        
               
       
    
