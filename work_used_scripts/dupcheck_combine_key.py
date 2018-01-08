#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import re
import shutil
import subprocess
import pdb

#从下面的路径中搜索并建立两个集合, 读值集合和打印集合
#field_get_value_set, field_print_set
dupCheckLuaPath="/home/ut/work/src/ob_dev/openbilling60_cmcc/mediation/dupcheck/lua"

lua_file_pat=re.compile(r"\w+\.lua")

field_get_value_set={}

field_getvalue_pat=re.compile(r"get_struct_value")
field_var_pat=re.compile(r"t_[a-zA-Z0-9]+")
field_getvalue_pat2=re.compile(r"t_.+%>")

field_print_set={}

lua_print_pat=re.compile(r"lua_print")
lua_print_pat2=re.compile(r"lua_print.+\);")

for  root, dirs,files in os.walk(dupCheckLuaPath):
    for file in files:
        if not lua_file_pat.search(file):
            continue
            
        ORIG_FILE= open(root+'/'+file, "r")
        line = ORIG_FILE.readline()
        while(line):
            if field_getvalue_pat.search(line):
                field_var_search=field_var_pat.search(line)
                field_getvalue_search2=field_getvalue_pat2.search(line)
                if field_var_search:
                    field_name=field_var_search.group()
                else:
                    line = ORIG_FILE.readline()
                    continue
                    
                if field_getvalue_search2:
                    field_get_value=field_getvalue_search2.group()
                else:
                    line = ORIG_FILE.readline()
                    continue
                    
                if not field_get_value_set.has_key(field_name):
                        field_get_value_set[field_name]=field_get_value
                        
            else:
                if lua_print_pat.search(line):
                    field_var_search=field_var_pat.search(line)
                    lua_print_search2=lua_print_pat2.search(line)
                    if field_var_search:
                        field_name=field_var_search.group()
                    else:
                        line = ORIG_FILE.readline()
                        continue
                        
                    if lua_print_search2:
                        lua_print=lua_print_search2.group()
                    else:
                        line = ORIG_FILE.readline()
                        continue
                        
                    if not field_print_set.has_key(field_name):
                        field_print_set[field_name]=lua_print
                       
            line = ORIG_FILE.readline()
        ORIG_FILE.close()    
    
    #add some new keys
    if not field_get_value_set.has_key('t_sInTrunkid'):
        field_get_value_set['t_sInTrunkid'] = \
        '''t_sInTrunkid = <% get_struct_value("pXdr","MXdr::SXdr.common.GSM_SPEC_INFO.IN_TRUNKID"); %>'''
            
#dup check keys combination is like this IMSI+START_TIME+CHARGING_ID+SGSN_ADDRESS
def parse_dup_check_deys_combine(keys_combine):
    key_pat=re.compile(r"\w+")
    keys = key_pat.findall(keys_combine)        
    return keys
    
    

import dupCheckKeyMap
dup_check_keys_combine=sys.argv.pop()
#pdb.set_trace()
keys=parse_dup_check_deys_combine(dup_check_keys_combine)
for key in keys:
    key = key.upper()
    if not dupCheckKeyMap.dup_check_key_map.has_key(key):
        print "%s is not found in dup_check_key_map set!!!"%(key)
        sys.exit()
        
funcName=sys.argv.pop()
        
print "============code for lua script============="        
print

if funcName is not None:
    print "function %s(t_sServiceId)"%(funcName)
    print "    lua_print(\"-----%s begin -----\");"%(funcName)
print "--[["
print "key: %s"%(dup_check_keys_combine)
print "--]]"

#定义变量
print "    local MD5KEY;"
for key in keys:
    key=key.upper()
    print "    local %s;"%(dupCheckKeyMap.dup_check_key_map[key])

#从话单读值
print
print "    --查重键"
for key in keys:
    key=key.upper()
    key_var=dupCheckKeyMap.dup_check_key_map[key]
    if not field_get_value_set.has_key(key_var):
        print "%s is not found in field_get_value_set set!!!"%(key_var)
        sys.exit()
    print "    %s"%(field_get_value_set[key_var])
    if "START_TIME" == key:
        print "    %s = lua_time2loc(%s);"%(key_var,key_var)
        print "    <%%set_struct_value('pNotify', \"MDupCheckDef::SNotify.STARTTIME\", %s); %%>"%(key_var)
        #print "<et_struct_value('pNotify', \"MDupCheckDef::SNotify.%s\", %s); >"%(key, key_var)

#打印获取的值
print
for key in keys:
    key=key.upper()
    key_var=dupCheckKeyMap.dup_check_key_map[key]
    if "t_sRESERVE1" == key_var or "t_sMocId" == key_var or \
       "t_iValidTimes" == key_var or "t_sAppNi" == key_var or "t_sDuration" == key_var or \
       "t_sInTrunkid" == key_var  or "t_sPartialNum" == key_var:
        continue 

    if not field_print_set.has_key(key_var):
        print "%s is not found in field_print_set set!!!"%(key_var)
        sys.exit()
    print "    %s"%(field_print_set[key_var])

#MD5Key
print
print "    --%s"%(dup_check_keys_combine)
print_MD5 = "MD5KEY = "
for key in keys:
    key=key.upper()
    key_var=dupCheckKeyMap.dup_check_key_map[key]
    print_MD5 += key_var + " .. t_sFchar .. "
 
end_pat=re.compile(r" .. t_sFchar .. $")
print_MD5 = end_pat.sub(";", print_MD5)
print "    %s"%(print_MD5)
print

print "    lua_print(\"MD5KEY = %s\", MD5KEY);"
print "    <%set_struct_value(\"pXdr\", \"MXdr::SXdr.FEATURE_CODE\", MD5KEY); %>"
print

processAccid=\
    "---mdb云化路由时使用-----\n\
    local t_iAccId = lua_set_md5(pNotify, MD5KEY);\n\
    lua_print(\"t_iAccId = %lld\", t_iAccId);\n\
    if(0 == t_iAccId) then\n\
      t_iAccId = 2003;--路由维度不能等于0，设置一个非零值\n\
    end\n\
    <%set_struct_value('pNotify', \"MDupCheckDef::SNotify.acct_id\", t_iAccId); %>\n\
    --------end------\n"
print "    %s"%(processAccid)
if funcName is not None:
    print "    lua_print(\"-----%s end -----\");"%(funcName)
    print "end  --function %s"%(funcName)
print
    
