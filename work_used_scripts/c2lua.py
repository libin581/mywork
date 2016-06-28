#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re
import pdb
import subprocess
import string
 
left_dakuohao_pat  = re.compile(r"^\s+{")
right_dakuohao_pat = re.compile(r"^\s+}")
goto_err_deal_pat  = re.compile(r"goto\s+err_deal;")
change_line_pat    = re.compile(r"\r\n$|\r$|\n$")

itoa_pat           = re.compile(r"itoa")
llpad_pat          = re.compile(r"llpad")
rlpad_pat          = re.compile(r"rlpad")
substr_pat         = re.compile(r"substr")
atoi_pat           = re.compile(r"atoi|atoi64")
strlen_pat         = re.compile(r"strlen")
t_sOutRecord_pat   = re.compile(r"t_sOutRecord")
gethosttime_pat    = re.compile(r"gethosttime")
gettime_pat        = re.compile(r"gettime")
trimx_pat          = re.compile(r"trimx")

comment_line_pat = re.compile(r"^--|^\s+--")
def skipCommentLine(line):
    if comment_line_pat.search(line):
        return True
    else:
        return False

space_header_pat = re.compile(r"^\s+") #行开头的空白部分
def getSpaceHeader(line):
    space_header_search = space_header_pat.search(line)
    space_header = nil
    if space_header_search:
        space_header = space_header_search.group()
    return space_header
        
def removeChangeLineSymbol(line):
    line = change_line_pat.sub("", line)
    return line
        
space_tail_pat = re.compile(r"\s+$") #行尾部的空格
def removeSpaceTail(line):
    line = space_tail_pat.sub("", line)
    return line
     
tab_pat = re.compile(r"\t") #tab键
def tabTo4Space(line_list):
    
    for i, line in enumerate(line_list):
        line = tab_pat.sub("    ",line)
        line_list[i] = line

def add_comment_symbol(line):
    space_header_pat           = re.compile(r"^\s+") #行开头的空白部分
    space_header_search = space_header_pat.search(line)
    if space_header_search:
        [start, end] = space_header_search.span()
        space_header = line[start:end]
        comment_part = line[end:]
        line = space_header+"--"+comment_part
    else:
        line = "--"+line
        
    return line
                    
def commentConvert(line_list):
    line_comment_pat           = re.compile(r"//") #行注释
    section_comment_start_pat  = re.compile(r"/\*") #段注释开始
    section_comment_end_pat    = re.compile(r"\*/") #段注释结束
    
    section_comment_start = 0
    for i, line in enumerate(line_list):
        if section_comment_start == 0:
            section_comment_start_search = section_comment_start_pat.search(line)
            if section_comment_start_search:
                section_comment_start = 1
                line = add_comment_symbol(line)
        else:
            section_comment_end_search = section_comment_end_pat.search(line)
            if section_comment_end_search:
                section_comment_start = 0
                line = add_comment_symbol(line)
            else:
                line = add_comment_symbol(line)
    
        if section_comment_start == 0:
                line = line_comment_pat.sub("--",line)
                
        line_list[i] = line    
           
def ifConvert(line_list):
    if_pat             = re.compile(r"if |if\(")
    else_pat           = re.compile(r"else")
    left_bigbrace_pat  = re.compile(r"\{")
    right_bigbrace_pat = re.compile(r"\}")
    comment_pat        = re.compile(r"--.+")
    
    if_floor = 0;
    for i, line in enumerate(line_list):
        if skipCommentLine(line) == True:
            continue
    
        if_search = if_pat.search(line)
        else_search = else_pat.search(line)
        left_bigbrace_search=""
        right_bigbrace_search=""
        if if_floor != 0:
            left_bigbrace_search  = left_bigbrace_pat.search(line)
            right_bigbrace_search = right_bigbrace_pat.search(line)
            
        if if_floor == 0:
            if if_search:
                if not else_search:
                    if_floor = if_floor + 1
                left_bigbrace_search = left_bigbrace_pat.search(line)
                if left_bigbrace_search:
                    line = left_bigbrace_pat.sub("then", line)
                line_list[i] = line  
                continue
        else:
            #pdb.set_trace()
            # 只有左大括号
            if left_bigbrace_search and not else_search and not if_search:
                last_line = line_list[i-1];
                last_line_else_search = else_pat.search(last_line)
                last_line_if_search   = if_pat.search(last_line)

                #pdb.set_trace()
                if last_line_else_search and not last_line_if_search:
                    line_list[i] = ""#del line_list[i]
                    continue
                    
                comment_search     = comment_pat.search(last_line)
                change_line_search = change_line_pat.search(last_line)
                if comment_search:
                    start = comment_search.start()
                    part1 = last_line[:start]
                    part1 = removeSpaceTail(part1)
                    part2 = last_line[start:]
                else:
                    start = change_line_search.start()
                    part1 = last_line[:start]
                    part1 = removeSpaceTail(part1)
                    part2 = last_line[start:]
                #pdb.set_trace()
                last_line = part1 + " then" + part2
                line_list[i-1] = last_line;
                line_list[i] = "" #del line_list[i]
                continue
                    
            #else {
            if left_bigbrace_search and else_search and not if_search and not right_bigbrace_search:
                line = left_bigbrace_pat.sub("", line)
                line_list[i] = line
                continue
                  
            #} else {
            if left_bigbrace_search and else_search and not if_search and right_bigbrace_search:
                line = left_bigbrace_pat.sub("", line)
                line = right_bigbrace_pat.sub("", line)
                line = else_pat.sub("else",line)
                line_list[i] = line
                continue
                  
            #else if {
            if left_bigbrace_search and if_search and not right_bigbrace_search:
                line = left_bigbrace_pat.sub("then", line)
                if not else_search:
                    if_floor = if_floor + 1
                line_list[i] = line
                continue
                    
            # } else 
            if right_bigbrace_search and else_search and not if_search:
                line = right_bigbrace_pat.sub("", line)
                line = else_pat.sub("else",line)
                line_list[i] = line
                continue
            
            # } else if {
            if right_bigbrace_search and else_search and if_search:
                line = right_bigbrace_pat.sub("", line)
                line = left_bigbrace_pat.sub("then", line)
                line = else_pat.sub("else",line)
                line_list[i] = line
                continue
                
              
            #只有右大括号 
            #if i > 76:
            #    pdb.set_trace()
            if right_bigbrace_search  and not else_search and not if_search:
                #如果下一行有else，则不替换为end， 直接删除此行
                if (i+1) < len(line_list):
                    next_line = line_list[i+1]
                    next_line_else_search = else_pat.search(next_line)
                    next_line_right_bigbrace_search = right_bigbrace_pat.search(next_line)
                    #下一行只有else, 没有{
                    if next_line_else_search and not next_line_right_bigbrace_search:
                        line_list[i] = "" #del line_list[i]
                        continue
                
                line = right_bigbrace_pat.sub("end", line)
                line_list[i] = line
                if_floor = if_floor - 1
                continue
            
            #if 前面没有else
            if if_search and not else_search:
                if_floor = if_floor + 1
                left_bigbrace_search = left_bigbrace_pat.search(line)
                if left_bigbrace_search:
                    line = left_bigbrace_pat.sub("then", line)
                line_list[i] = line  
                continue
            
        line_list[i] = line  
    
    if if_floor != 0:
        print "%s"%("括号不匹配\n")
    
    #else if 转为 elseif
    else_if_pat = re.compile(r"else if")
    for i, line in enumerate(line_list):
        line = else_if_pat.sub("elseif", line)
        line_list[i] = line
       

fenhao_pat=re.compile(r"\s+\;")
def removeNullExpress(line_list):
    for i, line in enumerate(line_list):
        if fenhao_pat.search(line):
            line_list[i] = "" #del line_list[i]
            continue
    
and_pat = re.compile(r"\&\&") #&& ==> and 
or_pat = re.compile(r"\|\|")   # || ==> or 
not_pat = re.compile(r"\!")   # !  ==> not
notequal_pat = re.compile(r"\!\=")  # ！= ==> ~=
and_space_pat= re.compile(r"\&\&\s+")
or_space_pat = re.compile(r"\|\|\s+")  
def symbolConvert(line_list):
    for i, line in enumerate(line_list):
        if skipCommentLine(line) == True:
            continue
        if and_space_pat.search(line):
            line = and_pat.sub("and", line)
        else:
            line = and_pat.sub("and ", line)
            
        if or_space_pat.search(line):
            line = or_pat.sub("or", line)
        else:
            line = or_pat.sub("or ", line)
            
        line = notequal_pat.sub("~=", line)
        not_search = not_pat.search(line)
        notequal_search = notequal_pat.search(line)
        if not_search and not notequal_search:
            line = not_pat.sub("not ", line)
        line_list[i] = line
    
trimx_pat = re.compile(r"trimx\(\w+, \"\s+\"\)")
var_pat = re.compile(r"\w+")
data_pat = re.compile(r"\d+")
strlen_pat = re.compile(r"strlen")
#substr_pat = re.compile(r"substr\(\w+.+\d+.+\d+\)")
substr_pat = re.compile(r"substr.+\w+.+\d+.+\d+.+")
#substr(t_sServiceCode, 0, strlen(t_sServiceCode)-1);
substr_sublen_pat = re.compile(r"substr\(\w+, \d+, string\.len\(\w+\)\-\d+\)")
#connect_pat = re.compile(r"\"\s+\+" | "\"\+" | "+\s+\"" | "+\"")
goto_err_deal_pat=re.compile(r"goto\s+err_deal")
def stringConvert(line_list):
    for i, line in enumerate(line_list):
        trimx_search = trimx_pat.search(line)
        strlen_search = strlen_pat.search(line)
        substr_search = substr_pat.search(line)
        #connect_search = connect_pat.search(line)
        atoi_search = atoi_pat.search(line)
        itoa_search = itoa_pat.search(line)
        rlpad_search = rlpad_pat.search(line)
        llpad_search = llpad_pat.search(line)
        gettime_search=gettime_pat.search(line)
        goto_err_deal_search=goto_err_deal_pat.search(line)
        
        #atoi ==> tonumber
        if atoi_search:
            str_dst = "tonumber"
            line = atoi_pat.sub("%s"%(str_dst), line)
            line_list[i] = line
        
        #itoa ==> tostring
        if itoa_search:
            str_dst = "tostring"
            line = itoa_pat.sub("%s"%(str_dst), line)
            line_list[i] = line
        
        #rlpad ==> l_rpad
        if rlpad_search:
            str_dst = "l_rpad"
            line = rlpad_pat.sub("%s"%(str_dst), line)
            line_list[i] = line
            
        #llpad ==> l_lpad
        if llpad_search:
            str_dst = "l_lpad"
            line = llpad_pat.sub("%s"%(str_dst), line)
            line_list[i] = line
        
        #gettime ==> libluabaseD.gettime
        if gettime_search:
            str_dst = "libluabaseD.gettime"
            line = gettime_pat.sub("%s"%(str_dst), line)
            line_list[i] = line
        
        #goto err_deal ==>
        #return RplCommon.error_deal(pSubCommon, t_sErrNo);
        if goto_err_deal_search:
            #pdb.set_trace()
            str_dst="return RplCommon.error_deal(pSubCommon, t_sErrNo)"
            line=goto_err_deal_pat.sub("%s"%(str_dst), line)
            line_list[i] = line
        
        #trimx(t_sServiceCode, " "); ==>
        #t_sServiceCode = string.gsub(t_sServiceCode, " ", "");
        if trimx_search:
            #pdb.set_trace()
            [func,trimx_var] = var_pat.findall(trimx_search.group())
            str_dst = " string.gsub("+trimx_var+''', " ", "")'''
            line = trimx_pat.sub("%s"%(str_dst), line)
            line_list[i] = line
            continue
            
        # strlen(t_sServiceCode) ==> string.len(t_sServiceCode)
        if strlen_search:
            line = strlen_pat.sub("string.len", line)
            
        # substr(t_sOppNumber, 5, 2) ==> string.sub(t_sOppNumber, 6, 7) 
        if substr_search:
            substr_ret = substr_search.group()
            vars_len=len(var_pat.findall(substr_ret))
            if vars_len == 4:
                [func, var, para2, para3] = var_pat.findall(substr_ret)
                para2_ = "%d"%(string.atoi(para2, 10) + 1)
                para3_ = "%d"%(string.atoi(para3, 10) + string.atoi(para2, 10))
                line = substr_pat.sub("string.sub(%s, %s, %s);"%(var, para2_, para3_), line)
        
        #substr(t_sServiceCode, 0, strlen(t_sServiceCode)-1) ==>
        #string.sub(t_sServiceCode, 1, strlen(t_sServiceCode)-1)
        substr_sublen_search = substr_sublen_pat.search(line)
        if substr_sublen_search:
            substr_sublen_ret = substr_sublen_search.group()
            #pdb.set_trace()
            [substr, var, data1, string_, length, var, data2] = var_pat.findall(substr_sublen_ret)
            data1_ = "%d"%(string.atoi(data1, 10) + 1)
            data2_ = "%d"%(string.atoi(data2, 10) - string.atoi(data1, 10))
            str_dst = "string.sub(%s, %s, string.len(%s)-%s)"%(var, data1_, var, data2_)
            line = substr_sublen_pat.sub("%s"%str_dst, line)
        
        line_list[i] = line
        
def valueGetConvert(line_list):
    #从下面的路径中搜索并建立读值集合field_get_value_set
    dupCheckLuaPath="/home/ut/work/openbilling60_cmcc/rating_billing/rating/upload/checker/rule/"

    lua_file_pat=re.compile(r"\w+\.lua")

    field_get_value_set={}

    field_getvalue_pat=re.compile(r"get_struct_value")
    field_var_pat=re.compile(r"t_[a-zA-Z0-9]+")
    field_getvalue_pat2=re.compile(r"t_.+%>")

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
                        field_get_value_set[field_name]=tab_pat.sub("    ",field_get_value)
                           
                           
                line = ORIG_FILE.readline()
            ORIG_FILE.close()    
        
    #add some new keys
    #if not field_get_value_set.has_key('t_sInTrunkid'):
    #    field_get_value_set['t_sInTrunkid'] = \
    #    '''t_sInTrunkid = <% get_struct_value("pXdr","MXdr::SXdr.common.GSM_SPEC_INFO.IN_TRUNKID"); %>'''

    GetXdrValue_pat=re.compile(r"GetXdrStrValue|GetXdrIntValue")
    field_getvalue_pat_line=re.compile(r"t_.+\)\;")
    for i, line in enumerate(line_list):
        if skipCommentLine(line) == True:
            continue
            
        if GetXdrValue_pat.search(line):
            #pdb.set_trace()
            field_var_search=field_var_pat.search(line)
            if field_var_search:
                field_name=field_var_search.group()
                if field_get_value_set.has_key(field_name):
                    line=field_getvalue_pat_line.sub(field_get_value_set[field_name],line)
                    line_list[i] = line   
                
                    
        
#------------main func-------------------------------------
file        = sys.argv.pop()
READ_FILE   = open(file, "r")
WRITE_FILE  = open(file+".lua", "w")
      
#格式处理
#subprocess.call(["/usr/bin/astyle", file])
    
line_list = []
line = READ_FILE.readline()
while(line):
    line_list.append(line)
    line = READ_FILE.readline()
READ_FILE.close()
    
#tab转成4个空格
tabTo4Space(line_list)

#注释行处理
commentConvert(line_list)

#处理if语句
ifConvert(line_list)

#只有";"的空语句
removeNullExpress(line_list)

# && ==> and 
# || ==> or 
# !  ==> not
# ！= ==> ~=
symbolConvert(line_list)

#字符串处理
stringConvert(line_list)

#获取XDR变量值GetXdrStrValue/GetXdrIntValue==>get_struct_value
valueGetConvert(line_list)

for i, line in enumerate(line_list):
    WRITE_FILE.write(line)
WRITE_FILE.close()

    