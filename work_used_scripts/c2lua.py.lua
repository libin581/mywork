#not  /usr/bin/python
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
string.len_pat         = re.compile(r"string.len")
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
     
def tabTo4Space(line_list):
    tab_pat = re.compile(r"\t") #tab键
    
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
    line_comment_pat           = re.compile(r"--") #行注释
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
    if_pat             = re.compile(r"if ")
    else_pat           = re.compile(r"else")
    right_bigbrace_pat = re.compile(r"\end")
    comment_pat        = re.compile(r"--.+")
    
    if_floor = 0;
    for i, line in enumerate(line_list):
        if skipCommentLine(line) == True:
            continue
    
        if_search = if_pat.search(line)
        else_search = else_pat.search(line)
        if if_floor ~= 0:
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
                    
            #else 
            if left_bigbrace_search and else_search and not if_search and not right_bigbrace_search:
                line = left_bigbrace_pat.sub("", line)
                line_list[i] = line
                continue
                  
            # else 
            if left_bigbrace_search and else_search and not if_search and right_bigbrace_search:
                line = left_bigbrace_pat.sub("", line)
                line = right_bigbrace_pat.sub("", line)
                line = else_pat.sub("else",line)
                line_list[i] = line
                continue
                  
            #elseif then
            if left_bigbrace_search and if_search and not right_bigbrace_search:
                line = left_bigbrace_pat.sub("then", line)
                if not else_search:
                    if_floor = if_floor + 1
                line_list[i] = line
                continue
                    
            #  else 
            if right_bigbrace_search and else_search and not if_search:
                line = right_bigbrace_pat.sub("", line)
                line = else_pat.sub("else",line)
                line_list[i] = line
                continue
            
            #  elseif then
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
                    #下一行只有else, 没有
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
    
    if if_floor ~= 0:
        print "%s"%("括号不匹配\n")
    
    #elseif 转为 elseif
    else_if_pat = re.compile(r"elseif")
    for i, line in enumerate(line_list):
        line = else_if_pat.sub("elseif", line)
        line_list[i] = line
       

fenhao_pat=re.compile(r"\s+\;")
def removeNullExpress(line_list):
    for i, line in enumerate(line_list):
        if fenhao_pat.search(line):
            line_list[i] = "" #del line_list[i]
            continue
    
and_pat = re.compile(r"\&\&") #and ==> and 
or_pat = re.compile(r"\|\|")   # or ==> or 
not_pat = re.compile(r"\not ")   # not   ==> not
notequal_pat = re.compile(r"\not \=")  # ！= ==> ~=
def symbolConvert(line_list):
    for i, line in enumerate(line_list):
        if skipCommentLine(line) == True:
            continue
        line = and_pat.sub("and", line)
        line = or_pat.sub("or", line)
        line = notequal_pat.sub("~=", line)
        not_search = not_pat.search(line)
        notequal_search = notequal_pat.search(line)
        if not_search and not notequal_search:
            line = not_pat.sub("not ", line)
        line_list[i] = line
    
trimx_pat = re.compile(r"trimx\(\w+, \"\s+\"\)")
var_pat = re.compile(r"\w+")
data_pat = re.compile(r"\d+")
string.len_pat = re.compile(r"string.len")
substr_pat = re.compile(r"substr\(\w+, \d+, \d+\)")
#string.sub(t_sServiceCode, 1, string.len(t_sServiceCode)-1);
substr_sublen_pat = re.compile(r"substr\(\w+, \d+, string\.len\(\w+\)\-\d+\)")
#connect_pat = re.compile(r"\"\s+\+" | "\"\+" | "+\s+\"" | "+\"")
def stringConvert(line_list):
    for i, line in enumerate(line_list):
        trimx_search = trimx_pat.search(line)
        string.len_search = string.len_pat.search(line)
        substr_search = substr_pat.search(line)
        #connect_search = connect_pat.search(line)
        
        # string.gsub(t_sServiceCode, " ", ""); ==>
        #t_sServiceCode = string.gsub(t_sServiceCode, " ", "");
        if trimx_search:
            #pdb.set_trace()
            [func,trimx_var] = var_pat.findall(trimx_search.group())
            str_dst = " string.gsub("+trimx_var+''', " ", "")'''
            line = trimx_pat.sub("%s"%(str_dst), line)
            line_list[i] = line
            continue
        # string.len(t_sServiceCode) ==> string.len(t_sServiceCode)
        if string.len_search:
            line = string.len_pat.sub("string.len", line)
        # string.sub(t_sOppNumber, 6, 7) ==> string.sub(t_sOppNumber, 6, 7) 
        if substr_search:
            substr_ret = substr_search.group()
            [func, var, para2, para3] = var_pat.findall(substr_ret)
            para2_ = "%d"%(string.atoi(para2, 10) + 1)
            para3_ = "%d"%(string.atoi(para3, 10) + string.atoi(para2, 10))
            line = substr_pat.sub("string.sub(%s, %s, %s)"%(var, para2_, para3_), line)
        #string.sub(t_sServiceCode, 1, string.len(t_sServiceCode)-1) ==>
        #string.sub(t_sServiceCode, 1, string.len(t_sServiceCode)-1)
        substr_sublen_search = substr_sublen_pat.search(line)
        if substr_sublen_search:
            substr_sublen_ret = substr_sublen_search.group()
            #pdb.set_trace()
            [substr, var, data1, string_, len, var, data2] = var_pat.findall(substr_sublen_ret)
            data1_ = "%d"%(string.atoi(data1, 10) + 1)
            data2_ = "%d"%(string.atoi(data2, 10) - string.atoi(data1, 10))
            str_dst = "string.sub(%s, %s, string.len(%s)-%s)"%(var, data1_, var, data2_)
            line = substr_sublen_pat.sub("%s"%str_dst, line)
        
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

# and ==> and 
# or ==> or 
# not   ==> not
# ！= ==> ~=
symbolConvert(line_list)

#字符串处理
stringConvert(line_list)

for i, line in enumerate(line_list):
    WRITE_FILE.write(line)
WRITE_FILE.close()

    