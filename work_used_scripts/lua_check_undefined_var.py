#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re
import pdb
import subprocess
import string

def usage():
    print '''
    usage:
    lua_check_undefined_var.py            : help info
    lua_check_undefined_var.py -h         : help info
    lua_check_undefined_var.py --help     : help info
    lua_check_undefined_var.py *.lua      : *.lua is lua script
    eg: lua_check_undefined_var.py file.lua
    lua_check_undefined_var.py path       : check all lua scripts at this path
    '''


comment_line_pat = re.compile(r"^--|^\s+--")
def skipCommentLine(line):
    if comment_line_pat.search(line):
        return True
    else:
        return False
        
def isFunction(var, line):
    function_pat=re.compile(r"\W%s\("%(var))
    if function_pat.search(line):
        return True
    else:
        return False
        
def isInComments(var, line):
    comments_pat=re.compile(r"--.*%s"%(var))
    if comments_pat.search(line):
        return True
    else:
        return False
        
def isNumber(var):
    if var.isdigit() == True:
        return True
    elif var[:2] == "0x" or var[:2] == "0X":
        return True
    else:
        return False
        
def isInString(var, line):
    var_in_str_pat=re.compile(r"[\"\']{1}.*%s.*[\"\']{1}"%(var))
    var_in_connect_symbol_pat=re.compile(r"\.\.\s*%s\W+"%(var))
    if var_in_connect_symbol_pat.search(line):
        return False
    elif var_in_str_pat.search(line):
        return True
    else:
        return False
    
const_pat=re.compile(r"[A-Z_0-9]+")    
def isConstVar(var):
    const_search=const_pat.search(var)
    if const_search and const_search.group() == var:
        return True
    else:
        return False
        
reserveWords=[ \
"and",      "exec",    "not",
"assert",   "finally", "or",
"break",    "for",	   "pass",
"class",    "from",    "print",
"continue", "global",  "raise",
"def",	    "if",      "return",
"del",	    "import",  "try",
"elif",	    "in",	   "while",
"else",	    "is",	   "with",
"except",   "lambda",  "yield",
#following not standard reserve words 
"require",  "use",     "PXdr",
"elseif",   "do",      "setsdlval",
"getsdlval","getsdllen","setsdl",
"getsdl",   "g_pNotifyList", "g_pXdrList",
"key",      "libluabaseD", "pairs",
"nil",      "debug",    "source",
"math",     "iDoPrintInfo",
"set_struct_value", "get_struct_value",
"string",   "function", "true",
"false",    "k",      "v",
"i",        "arg",
"local",    "then",     "end",
"RplCommon",
"CONST_PROV_CODE",
"CONST_PROC_NO",
"CONST_FILE_DATE",
"CONST_RECORD_FLAG",
"CONST_DELETE_LATER",

#template var
#"t_iResult",
#"l_sFileType",    
#"l_lVolume",  
#"l_lUpVolume",    
#"l_lDnVolume",    
#"l_lDuration",    
#"l_sStartTime",   
#"l_sStopTime",    
#"l_lCfee",        
#"l_lLFee1",       
#"l_lLFee2",       
#"l_iBillFlag",    
#"l_iCallIndicate",
#"l_iReupFlag",

]

def isReserveWords(var):
    for word in reserveWords:
        if word == var:
            return True
    return False

def isDrtype(var):
    if var[:3]=="dr_":
        return True
    else:
        return False
    
local_var_def_pat=re.compile(r"^\s*local\s+(\w+)\s*=")
var_def_pat=re.compile(r"^\s*(\w+)\s*=")
func_pat=re.compile(r"\W+(\w+)\s*\(.+\)")
func_return_value_pat=re.compile(r"^\s*([\w,\s]+)\s*=\s*\w+\(")
ret_var_pat=re.compile(r"(\w+)")
function_def_pat=re.compile(r"function\s+\w+\(([\w,\s]+)\)")
def getDefinedVarAndFunc(line_list):
    defVar={}
    for i, line in enumerate(line_list):
        if skipCommentLine(line) == True:
            continue
            
        retVars1_tmp = local_var_def_pat.findall(line)
        retVars1 = []
        for var in retVars1_tmp:
            local_var_eq_nil_pat=re.compile(r"^\s*local\s+%s\s*=\s*nil"%(var))
            if not local_var_eq_nil_pat.search(line):
                retVars1.append(var)
        
        retVars2_tmp = var_def_pat.findall(line)
        retVars2 = []
        for var in retVars2_tmp:
            var_eq_var_pat=re.compile(r"^\s*%s\s*=\W*%s"%(var, var))
            var_eq_nil_pat=re.compile(r"^\s*%s\s*=.*nil"%(var))
            if not var_eq_var_pat.search(line) and \
               not var_eq_nil_pat.search(line):
                retVars2.append(var)
                
        retVars3 = func_pat.findall(line)
        retStr=func_return_value_pat.findall(line)
        retVars4=[]
        for var in retStr:
            #pdb.set_trace()
            retVars4+=ret_var_pat.findall(var)
        retStr = function_def_pat.findall(line)
        retVars5=[]
        for var in retStr:
            retVars5+=ret_var_pat.findall(var)
        retVars = retVars1+retVars2+retVars3+retVars4+retVars5
        
        for var in retVars:
            #pdb.set_trace()
            if not defVar.has_key(var):
                defVar[var] = ""
    return defVar
    
var_pat=re.compile(r"\W+(\w+)")
local_pat=re.compile(r"local\s+(\w+)")
local_function_pat=re.compile(r"local\s+function")
def getAllVars(line_list):
    var_times={}
    for i, line in enumerate(line_list):
        if skipCommentLine(line) == True:
            continue
            
        local_search = local_pat.search(line)
        local_function_search = local_function_pat.search(line)
        
        vars=[]
        retVars=var_pat.findall(line)
        
        for var in retVars:
            if isInString(var, line) == False and \
               isFunction(var, line) == False and \
               isInComments(var, line) == False:
                vars.append(var)
        
        #if not local_function_search and local_search:
        #    vars+=local_search.groups()
        
        for var in vars:
            if not (var == "") :
                if not var_times.has_key(var):
                    var_times[var]=1
                else:
                    var_times[var]+=1
    return var_times
            
def oneTimeVar(var_times):
    var_onetime = []
    for var in var_times.keys():
        if var_times[var] == 1:
            #isConstVar(var) == False and \
            if isNumber(var) == False and \
               isReserveWords(var) == False and \
               isConstVar(var) == False and \
               isDrtype(var) == False:
                var_onetime.append(var)
    return var_onetime
    
def undefVar(var_times, varDef_):
    undefVar = []
    for var in var_times.keys():
        if not varDef_.has_key(var) and \
           isNumber(var) == False and \
           isReserveWords(var) == False and \
           isConstVar(var) == False:
            undefVar.append(var)
    return undefVar
            
    
lua_pat=re.compile(r"\.lua$")
def isLuaScript(fileName):
    if lua_pat.search(fileName):
        return True
    else:
        return False
    
#------------main func-------------------------------------
file = ""
if len(sys.argv) == 1:
    usage()
    sys.exit()
elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    usage()
    sys.exit()
else:
    file = sys.argv.pop()

file_list=[]
if os.path.isfile(file):
    file_list.append(file)
elif os.path.isdir(file):
    workPath=file
    for  root, dirs,files in os.walk(workPath):
        for file in files:
            if isLuaScript(file):
                file_list.append(root+"/"+file)
else:
    print "%s is not file or dir!!!"%(file)

for file in file_list:
    line_list = []
    var_times = {}
    var_onetime = []
    
    READ_FILE   = open(file, "r")
    line = READ_FILE.readline()
    while(line):
        line_list.append(line)
        line = READ_FILE.readline()
    READ_FILE.close()

    #find all defined variables
    varDef_ = getDefinedVarAndFunc(line_list)
    
    #find all variables and used times
    var_times = getAllVars(line_list)

    #select one time occured variable and remove some special variable
    var_onetime = oneTimeVar(var_times)

    var_undef = undefVar(var_times, varDef_)
    
    #---------print the result----------
    print "------------------------------------------------------"
    print "file:%s"%(file)
    #if len(var_onetime) > 0:
    #    print "Following variables are refered only one time:"
    #    for var in var_onetime:
    #        print var
            
    if len(var_undef) > 0:
        print "Following variables are undefined:"
        for var in var_undef:
            print var
    print "------------------------------------------------------"
# end of file_list
