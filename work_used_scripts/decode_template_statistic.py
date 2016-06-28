#! /usr/bin/python

import os
import sys
import re
import pdb
from os.path import expanduser

#import convert_func_list
import catchConvertFuncNameFromCode

province=sys.argv.pop()
if province == "neimeng":
    import decode_template_neimeng as temp_list
elif province == "xizang":
    import temp_list_xizang as temp_list
elif province == "jiangxi":
    import decode_template_jiangxi as temp_list
elif province == "gansu":
    import decode_template_gansu as temp_list
elif province == "guizhou":
    import decode_template_guizhou as temp_list
else:
    print "unknow provinve %s"%(provinve)

def tempStatic(workpath_prov):
    tempnofoundlist=[]
    tempfoundlist=[]
    #pdb.set_trace()
    #rmspace=re.compile(r"^[0-9a-zA-Z].*dcd")
    for temp in temp_list.voiceTempList:
        #print "%s"%(temp)
        #rmspacesearch=rmspace.search(temp)

        #if rmspacesearch: 
        #    temp=rmspacesearch.group()
        #else:
        #    pdb.set_trace()
        #    print "error file format!!!"
        #    sys.exit()
        
        temp=temp.strip()

        if temp == "":
            continue
        
        
        isfound=False
        
        workpath_pub=workpath_prov+"../public/"
        for  root, dirs,files in os.walk(workpath_prov):
            for file in files:
                if file == temp:
                   isfound=True
                   break

        for  root, dirs,files in os.walk(workpath_pub):
            for file in files:
                if file == temp:
                   isfound=True
                   break

        if isfound == False:
           tempnofoundlist.append(temp)
        else:
           tempfoundlist.append(temp)

    print "==============template static======================"
    print "temp found:(%d)"%(len(tempfoundlist))
    for temp in tempfoundlist:
        #print "%s"%(temp)
        pass


    print "----------------------------"
    print "temp not found:(%d)"%(len(tempnofoundlist))
    for temp in tempnofoundlist:
        print "%s"%(temp)

def getTempInfoStatic(workpath_prov):
    comment_pat=re.compile(r"\s*//")
    service_id_pat=re.compile(r"RECORD_XDR_OUTPUT SERVICE_ID")
    dr_type_pat=re.compile(r"RECORD_XDR_OUTPUT DR_TYPE")
    number_pat=re.compile(r"[0-9]+")
    enter_pat=re.compile(r"\n|\r")
    comment_pat=re.compile(r"^//|^\s+//")
    record_list=[]
    for  root, dirs,files in os.walk(workpath_prov):
        for file in files:
            #pdb.set_trace()
            record={}
            record["filename"]=file
            ORIG_FILE= open(root+file, "r")
            line = ORIG_FILE.readline()
            file_head_coments=True
            serviceDesc=''
            service_id=''
            dr_type=''
            record["serviceDesc"]=serviceDesc
            record["serviceId"]=service_id
            record["drType"]=dr_type
            while (line):
                if file_head_coments==True:
                    comment_pat_search=comment_pat.search(line)
                    if comment_pat_search:
                        end=comment_pat_search.end()
                        enter_pat_search=enter_pat.search(line)
                        if enter_pat_search:
                            start=enter_pat_search.start()
                        if serviceDesc=='':
                            serviceDesc=line[end:start]
                        else:
                            serviceDesc+=','+line[end:start]
                    else:
                        file_head_coments=False
                        record["serviceDesc"]=serviceDesc
                     
                if service_id_pat.search(line):
                    if not comment_pat.search(line):
                        number_pat_search=number_pat.search(line)
                        if number_pat_search:
                            (start, end)=number_pat_search.span()
                            if service_id=='':
                                service_id=line[start:end]
                            elif not service_id==line[start:end]:
                                service_id+=','+line[start:end]
                            record["serviceId"]=service_id
                
                if dr_type_pat.search(line):
                    if not comment_pat.search(line):
                        number_pat_search=number_pat.search(line)
                        if number_pat_search:
                            (start, end)=number_pat_search.span()
                            if dr_type=='':
                                dr_type=line[start:end]
                            elif not dr_type==line[start:end]:
                                dr_type+=','+line[start:end]     
                            record["drType"]=dr_type
                        
                line = ORIG_FILE.readline()
            ORIG_FILE.close()    
            record_list.append(record)

    for record in record_list:
        print "%35s     %30s     %20s     %s"%(record["filename"],\
              record["serviceId"], record["drType"], record["serviceDesc"])
        
def funcStatistics(workpath_prov):
    sourceFilePath="/home/ut/work/openbilling60_cmcc/rating_billing/rating/decode/tuning/Ng/"
    convertFuncList=catchConvertFuncNameFromCode.catchConvertFuncName(sourceFilePath)
    notfoundfunclist=[]
    #rmspace=re.compile(r"^[0-9a-zA-Z].*dcd")
    for temp in temp_list.voiceTempList:
        #rmspacesearch=rmspace.search(temp)
        #if rmspacesearch: 
        #    temp=rmspacesearch.group()
        #else:
        #    print "error file format!!!"
        #    sys.exit()
        #    
        temp=temp.strip()
        
        isfound = False
        for  root, dirs,files in os.walk(workpath_prov):
                for file in files:
                    if file == temp:
                       isfound=True
                       break
                       
        if isfound == False:
           #print "%s is not found!!!"%(temp)
           continue

        ORIG_FILE= open(workpath_prov+temp, "r")
        line = ORIG_FILE.readline()
        convertfind= re.compile(r"RECORD_CONVERT_FUNC")
        comment=re.compile(r"^\s*//")
        
        while line:
            if not convertfind.search(line):
               line = ORIG_FILE.readline()
               continue

            if comment.search(line):
               line = ORIG_FILE.readline()
               continue
                
            #if temp=="d_gsm.dcd":
            #   pdb.set_trace()        
            enter_pat=re.compile(r"\n")
            if enter_pat.search(line):
              line=enter_pat.sub("", line)

            equal_pat = re.compile(r"=")
            idx=equal_pat.search(line).start()
            convertFunc=line[idx + 2:]

            space_pat = re.compile(r"\s+")
            spacesearch= space_pat.search(convertFunc)
            if spacesearch:
               idx=spacesearch.start()
               convertFunc=convertFunc[:idx]

            #if convertFunc=="convert_split_mvno":
            #   pdb.set_trace()        

            isFound=False
            for func in convertFuncList:
                if func == convertFunc:
                   isFound=True
                   break

            if  isFound == False:
                isexist = False
                for func in notfoundfunclist:
                   if func == convertFunc:
                      isexist = True
                      break
                
                if isexist == False:
                   notfoundfunclist.append(convertFunc);

            line = ORIG_FILE.readline()
        ORIG_FILE.close()
            
    print "==============convert func static======================"
    print "func not found:(%d)"%(len(notfoundfunclist))
    for func in notfoundfunclist:
        print "%s"%(func)



def service_processFile(file):
    result=file
    grepRes = os.popen('grep -i "service_id" %s'%(file)) 
    grepResR=grepRes.read() 

    service_id_pat = re.compile(r"[0-9]{5}")
    service_id_search = service_id_pat.search(line)
    serviceId=[]
    if service_id_search:
        serviceId.append(service_id_search.group())
    else:
        print "%s has no service id!!!"%(file)
        return

    firstItem=serviceId[0]
    for item in serviceId:
      if item != firstItem:
        print "%s has different service id!!!"%(file)
        return

    

    #if service_hash.haskey(firstItem)
    #    return

import service_list
 
def serviceStatistics():
    resultlist=[]
    workpath1=workpath
    if province == "neimeng":
        workpath1 +="nm/"
    elif province == "xizang":
        workpath1 += "xz/"
    else:
        print "unknown province!!!"
        sys.exit()
    
    for root, dirs, files in os.walk(workpath1):
        for file in files:    
            result = service_processFile(file)
            resultlist=resultlist.append(result)

    workpath2=workpath+"public/"
    for root, dirs, files in os.walk(workpath2):
        for file in files:    
            result = service_processFile(file)
            resultlist=resultlist.append(result)

#######################################################
#temp = "d_gsm.dcd"
HomeDir = expanduser('~')
workpath=HomeDir+"/work/openbilling60_cmcc/rating_billing/rating/decode/template/"
workpath_prov=workpath
if province == "neimeng":
    workpath_prov +="nm/"
elif province == "xizang":
    workpath_prov += "xz/"
elif province == "jiangxi":
    workpath_prov += "jx/"
elif province == "gansu":
    workpath_prov += "gs/"
elif province == "guizhou":
    workpath_prov += "gz/" 
else:
    print "unknown province!!!"
    sys.exit()


tempStatic(workpath_prov)
#getTempInfoStatic(workpath_prov)
funcStatistics(workpath_prov)





