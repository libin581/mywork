#! /usr/bin/python

import sys
import os
import re
import shutil
import subprocess
import pdb

hashTable={
"zj_convert_bxf_dfile":"//",
"convert_bxf_dfile":"//",
"FIELD_DUP_XDR_FIELD":"//",
"FIELD_XDRKEY = \"RECORD_TYPE\"":"FIELD_XDRKEY = record_type",
#"guangxi_convert_gsm_split_merge_by_sequenceno":"convert_gsm_split_merge_by_sequenceno",
"str2str_untilChar":"str2str_gxUntilChar",
#"RECORD_XDR_OUTPUT IMSI_HEAD = 46007;46005;46006":"//RECORD_XDR_OUTPUT IMSI_HEAD = 46007;46005;46006",
"ASASNONENE":"BER   //ASASNONENE",
"RECORD_XDR_OUTPUT \"RECORD_TYPE\"":"RECORD_XDR_OUTPUT record_type",
"\"JF.NM.IP.CHINAMOBILE\"":"JF.NM.IP.CHINAMOBILE",
"gansu_guangxi_convert_gsm_sequenceno_ericsson":"convert_gsm_sequenceno_ericsson",
}

changedFileList=[]
nonchangedFileList=[]

def processFile(file):
    #pdb.set_trace()
    ORIG_FILE= open(origPath+file, "r")
    DEST_FILE= open(destPath+file, "w")
    line = ORIG_FILE.readline()
    isFound=False
    comment=re.compile(r"^//|^\s+//")
    convertFunc=re.compile(r"RECORD_CONVERT_FUNC")

    while line:
        line_add = []
        #if convertFunc.search(line):
        if not comment.search(line):
            for (origstr, deststr) in hashTable.items():
                pat = re.compile(r"%s"%(origstr))
                found=pat.search(line)
                if found:
                    isFound=True
                    if deststr == "//":
                        if convertFunc.search(line):
                            idx=convertFunc.search(line).start()
                            part1=line[0:idx]
                            part2=line[idx:]
                            line=part1+"//"+part2
                        
                        dup_xdr_name_pat = re.compile(r"FIELD_DUP_XDR_FIELD_NAME")
                        if dup_xdr_name_pat.search(line):
                            (startIdx,endIdx)=dup_xdr_name_pat.search(line).span()
                            line_add.append(line[:startIdx]+"FIELD_SECOND_XDRKEY"+line[endIdx:])

                        dup_xdr_pat = re.compile(r"FIELD_DUP_XDR_FIELD")
                        if dup_xdr_pat.search(line):
                            idx=dup_xdr_pat.search(line).start()
                            part1=line[0:idx]
                            part2=line[idx:]
                            line=part1+"//"+part2

                    else:
                        pat_other=re.compile(r"neimeng_%s"%(origstr))
                        if not pat_other.search(line):
                           line=pat.sub(deststr,line)
                    break

            #add space between funcname and "//"
        if not comment.search(line):
            space_comment_pat=re.compile(r"//")
            space_comment_search=space_comment_pat.search(line)
            if space_comment_search:
                (start,end)=space_comment_search.span()
                part1=line[0:start]
                part2=line[end:]
                end_space=re.compile(r"\s+$")
                end_space_search=end_space.search(part1)
                if end_space_search:
                    part1=end_space.sub("",part1)
                line=part1+"    //  "+part2

        #convert tab to space 
        #if convertFunc.search(line):
        #pdb.set_trace()
        tab=re.compile(r"\t")
        tabsearch=tab.search(line)
        if tabsearch:
            line=tab.sub("        ", line)
        space=re.compile(r"\s+RECORD_CONVERT_FUN")
        spacesearch=space.search(line)
        if spacesearch:
            line=space.sub("                RECORD_CONVERT_FUN",line)

        DEST_FILE.write("%s" % (line))
        for idx in range(0,len(line_add),1):
             DEST_FILE.write("%s" % (line_add[idx]))

        line = ORIG_FILE.readline()
    ORIG_FILE.close()
    DEST_FILE.close()

    if isFound == True:
       changedFileList.append(file)
    else:
       nonchangedFileList.append(file)
	   

#================================================
province=sys.argv.pop()
workPath="/home/ut/work/billing40/app30/filter/template"
#print "%s" % (workPath)
origPath=workPath+"/"+province+"_60/"
destPath=workPath+"/"+province+"_60_mini_modi/"

os.chdir(workPath)
if os.path.isdir(destPath):
   shutil.rmtree(destPath)
os.mkdir(destPath)


for root, dirs, files in os.walk(origPath):
    for file in files:    
       processFile(file)

#print "Following files are changed: "
#for file in changedFileList:
#    print "%s"%(file)
#
#print "Following files are not changed: "
#for file in nonchangedFileList:
#    print "%s"%(file)

