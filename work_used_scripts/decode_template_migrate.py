#! /usr/bin/python

import subprocess
import os
import shutil
import sys
import re
import pdb

province=sys.argv.pop()
if province == "neimeng":
    import decode_template_neimeng as temp_list
elif province == "xizang":
    import decode_template_xizang as temp_list
elif province == "jiangxi":
    import decode_template_jiangxi as temp_list
elif province == "gansu":
    import decode_template_gansu as temp_list
elif province == "guizhou":
    import decode_template_guizhou as temp_list
else:
    print "unknow provinve %s"%(provinve)
    sys.exit()

workpath="/home/ut/work/billing40/app30/filter/template/"
workpath1=workpath+province
workpath2=workpath+province+"_60"
if os.path.isdir(workpath2):
    shutil.rmtree(workpath2)
os.mkdir(workpath2)

temps={}
for temp in temp_list.voiceTempList:
    #rmspace=re.compile(r"^[0-9a-zA-Z].*dcd")
    #rmspacesearch=rmspace.search(temp)
    
    #if rmspacesearch: 
    #    temp=rmspacesearch.group()
    #    if temps.has_key(temp):
    #        print "template is repeated: %s"%(temp)
    #        continue
    #    else:
    #        temps[temp]="";
    #else:
    #    print "error file format!!!temp(%s)"%(temp)
    #    sys.exit()

    temp=temp.strip()
    
    #pdb.set_trace()
    tempfound = False
    for  root, dirs,files in os.walk(workpath1):
            for file in files:
                if temp == file:
                   tempfound=True
                   break

    if tempfound == False:
        print "%s is not found!!!"%(temp)
        continue

    subprocess.call(["./replace.pl", workpath1+"/"+temp, workpath2+"/"+temp])


