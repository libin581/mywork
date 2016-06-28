#! /usr/bin/python
# -*- coding: utf-8 -*-
 
import time
import sys
import pdb
import string
import re

fileHeader = '''
-- $Id: file_name currentTime libin3 $  --
-- brief:
--
--

-------------------------------------全局变量定义--------------------------------------------
require "libluabaseD"

<% use("Xdr_app.MXdr::SXdr") %>
<% use("RplVarType.MRplVarType::SErrorInfo") %>

--SXdr.SCommon
local pCommon       = nil;
--SXdr.SCommon.SGsmSpecInfo
local pGsmSpecInfo  = nil;
--SXdr.SSubXdr.SSubCommon
local pSubCommon    = nil;
--SXdr.SSubXdr.SSubCommon.SUserInfoBase
local pUserInfo     = nil;
--SXdr.SSubXdr.SGsmInfo
local pGsmInfo      = nil;
--SXdr.SSubXdr.SSubCommon.SRatingResList
local pRatingResList    = nil;

local pMmsSpecInfo      = nil;
local pSmsSpecInfo      = nil;
local pIsmpSpecInfo     = nil;
    
local iDoPrintInfo      = 1;    --1:打印调试信息到log,  0:不打印调试信息到log

	
'''


init_getsdlval_func = '''
--[[============================================================================
--函数名称: init_getsdlval
--作    用: 初始化指针
--输入参数:
--输出参数:
--返回值：
--==========================================================================--]]
function init_getsdlval()
    if iDoPrintInfo == 1 then	
        RplCommon.print('----------init_getsdlval begin-------------');
    end
        
    pCommon = <%get_struct_value('PXdr',"MXdr::SXdr.COMMON") %>
    if pCommon == nil then
        if iDoPrintInfo == 1 then
            RplCommon.print('--init pCommon failed.--');
        end
        return -1;
    end

    pSubXdr = <%get_struct_value('PXdr',"MXdr::SXdr.TOTAL_XDR") %>
    if pSubXdr == nil then
        if iDoPrintInfo == 1 then
            RplCommon.print('----------init_getsdlval failed.-------------');
        end
        return -1;
    end
        
    ------  init pCommon  ------  
    pGsmSpecInfo    = <%get_struct_value('pCommon',"MXdr::SCommon.GSM_SPEC_INFO") %>
    pGsmInfo    = <%get_struct_value('pSubXdr',"MXdr::SSubXdr.GSM_INFO") %>
    pSubCommon  = <%get_struct_value('pSubXdr',"MXdr::SSubXdr.SUB_COMMON") %>
    pUserInfo   = <%get_struct_value('pSubCommon',"MXdr::SSubCommon.USER_BASE_INFO") %>
    pRatingResList  = <%get_sdl_ref('pSubCommon',"MXdr::SSubCommon.RATING_RES") %>      
    pSmsSpecInfo    = <%get_struct_value('pCommon',"MXdr::SCommon.SMS_SPEC_INFO") %>       
    pMmsSpecInfo    = <%get_struct_value('pCommon',"MXdr::SCommon.MMS_SPEC_INFO") %>
    pIsmpSpecInfo    = <%get_struct_value('pCommon',"MXdr::SCommon.ISMP_SPEC_INFO") %>

    if pGsmSpecInfo == nil or pGsmInfo == nil or 
        pSubCommon == nil or pUserInfo == nil or
        pRatingResList == nil or pSmsSpecInfo == nil or
        pMmsSpecInfo == nil or pIsmpSpecInfo == nil then
        if iDoPrintInfo == 1 then
            RplCommon.print('----------init_getsdlval failed.-------------');
        end
        return -1;
    end

    if iDoPrintInfo == 1 then
        RplCommon.print('----------init_getsdlval end-------------');
    end
    return 0;
end

'''

dealXdrFunc = '''
----[[============================================================================
----函数名称: dealXdr
----作    用: 逐条处理详单
----输入参数:
----输出参数:
----返回值：
----==========================================================================--]]
function dealXdr()
    if iDoPrintInfo == 1 then
        RplCommon.print('--------------------  dealXdr begin  --------------------------');
    end

    ------ 话单处理开始  ------
    --变量定义
    
    t_iResult	    = 0;
    l_sFileType 	= "CM";
    l_lVolume 	    = 0;
    l_lUpVolume 	= 0
    l_lDnVolume 	= 0;
    l_lDuration 	= t_iDuration ;
    l_sStartTime 	= t_sStartTime;
    l_sStopTime 	= "0";
    l_lCfee  		= 0;
    l_lLFee1 		= 0;
    l_lLFee2 		= 0;
    l_iBillFlag		= 0;
    l_iCallIndicate = 0;
    l_iReupFlag	    = 0;

    return;
    
end

'''
    
mainFunc = '''
--[[============================================================================
--函数名称: funcName()
--作    用: 业务处理入口
--输入参数:
--输出参数:
--返回值：
--==========================================================================--]]
function funcName()
    iDoPrintInfo = 1;
    if iDoPrintInfo == 1 then
        RplCommon.print('------------------------------funcName begin--------------------------------');
    end

    local iInitFlag	= 0;	
    iInitFlag = init_getsdlval();
    if iDoPrintInfo == 1 then
        RplCommon.print('---iInitFlag::' .. iInitFlag);
    end

    if iInitFlag == 0 then
        if iDoPrintInfo == 1 then
            RplCommon.print('-----------init success--------'); 
        end
        local iRet = dealXdr();	
        if iRet == -1 then
            return;
        end;
    else
        if iDoPrintInfo == 1 then
            RplCommon.print('-------init_getsdlval() failed.');
        end
    end
        
    if iDoPrintInfo == 1 then
        RplCommon.print('------------------------------funcName end--------------------------------');
    end
    return;
end

'''

def genCode():
    provice = 'jx'
  
    print "============code for lua script============="        
    print

    file_name = "upc_"+service+"_"+provice+".lua"

    ISOTIMEFORMAT='%Y-%m-%d %X'
    curTime = time.strftime( ISOTIMEFORMAT, time.localtime() )
    
    #pdb.set_trace()
    global fileHeader
    fileHeader = fileHeader.replace('currentTime', curTime)
    fileHeader = fileHeader.replace('file_name', file_name)
    print '%s'%(fileHeader)

    global init_getsdlval_func
    print "%s"%(init_getsdlval_func)

    global dealXdrFunc
    dealXdrFunc = dealXdrFunc.replace("CM", service.upper())
    print '%s'%(dealXdrFunc)

    mainFuncName = service+"_main"
    global mainFunc
    mainFunc = mainFunc.replace('funcName',mainFuncName)
    print '%s'%(mainFunc)

luaFilePath = "/home/libin3/work/openbilling60_cmcc/rating_billing/rating/upload/checker/rule/jx"
    
def checkCode(file):
    global luaFilePath
                
    #build variable-define table
    var_define = {}   
    comment_head_pat = re.compile(r"^\s+--")
    local_pat = re.compile(r"local.+=") 
    READ_FILE   = open(luaFilePath+'/'+file, "r")
    line = READ_FILE.readline()
    while(line):
        if comment_head_pat.search(line):
            line = READ_FILE.readline()
            continue
        
        local_search = local_pat.search(line)
        if local_search:
            local_var = local_search.group()
            local_var = string.replace(local_var, 'local',"",1)
            local_var = local_var.lstrip()
            local_var = string.replace(local_var, '=',"",1)
            local_var = local_var.rstrip()
            #pdb.set_trace()
            if not var_define.has_key(local_var):
                var_define[local_var] = ""
                
        line = READ_FILE.readline()
        
    READ_FILE.close()
    
    #pdb.set_trace()
    #check variable
    var_pat = re.compile(r"[^\w]{1}t_i[^a-z]{1}\w+|[^\w]{1}t_s[^a-z]{1}\w+|[^\w]{1}i[^a-z]{1}\w+|[^\w]{1}s[^a-z]{1}\w+")
    print "-------following var is not defined----------"
    READ_FILE   = open(luaFilePath+'/'+file, "r")
    line = READ_FILE.readline()
    while(line):
        if comment_head_pat.search(line):
            line = READ_FILE.readline()
            continue
        
        #pdb.set_trace()
        var_search = var_pat.search(line)
        if var_search:
            vars = var_pat.findall(line)
            for var in vars:
                var = var[1:]
                if not var_define.has_key(var):
                    print var+": "+line
    
        line = READ_FILE.readline()
        
    READ_FILE.close()
        
    #check function
    func_newfunc = {
    #    old func  <---->     new func
    #    ------------------------------    
        "itoa"       :       "tostring",
        "llpad"      :       "l_lpad",
        "rlpad"      :       "l_rpad",
        "substr"     :       "string.sub",
        "atoi"       :       "tonumber",
        "atoi64"     :       "tonumber",
        "strlen"     :       "string.len",
        "gethosttime":       "GetHostTimeR",
        "gettime"    :       "libluabaseD.gettime",
        "trimx"      :       "strtrim",
    }
    func_pats = []
    for key in func_newfunc.keys():
        func_pat = re.compile(key)
        func_pats.append(func_pat)
    #pdb.set_trace()
    print "-------following lines contain undefined function----------"
    READ_FILE = open(luaFilePath+'/'+file, "r")
    line = READ_FILE.readline()
    while(line):
        #pdb.set_trace()
        for func_pat in func_pats:
            if func_pat.search(line):
                print line
                #pdb.set_trace()
                break
        
        line = READ_FILE.readline()
    READ_FILE.close()    
        
def modifyCode(file):
    global luaFilePath
                
    comment_head_pat = re.compile(r"^\s+--")
    llike_pat = re.compile(r"llike")

    ORIG_FILE = open(luaFilePath+'/'+file, "r")
    DEST_FILE = open(luaFilePath+'/'+file+"~", "r")
    
    line = ORIG_FILE.readline()
    while(line):
        if comment_head_pat.search(line):
            DEST_FILE.write(line)
        
            line = ORIG_FILE.readline()
            continue
    
        llike_search = llike_pat.search(line)
        if llike_search:
            line = llike_pat.sub("string.find", line)
            
            
        line = ORIG_FILE.readline()    
        
    ORIG_FILE.close()
    DEST_FILE.close()
        
        
def help():
    usage = '''
    usage: 
    1. upload_check.py action service
    2. upload_check.py action file
        
    -- action: 
        -g:  generate code 
        -c:  check file
        -m:  modify
    '''
    print usage
    
#------------------------------------------------
if len(sys.argv) == 1:
    help()
    sys.exit()
elif len(sys.argv) == 2:
    print "input parameters is not enough"
else:
    action = sys.argv[1]
    if action == "-g":
        service = sys.argv[2]
        genCode()
    elif action == "-c":
        file = sys.argv[2]
        checkCode(file)
    elif action == "-m":
        file = sys.argv[2]
        modifyCode(file)
    else:
        print "invalid input parameter %s"%(action)
        

