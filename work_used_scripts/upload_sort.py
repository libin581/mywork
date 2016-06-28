#! /usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys

printFunc = '''
--============================================================================
--函数名称: RplCommon.print
--作    用: 输出信息到屏幕和日志文件
--输入参数: 日志信息
--输出参数: 无
--返回值：无
--============================================================================
function RplCommon.print(...)
    if DEBUG == 0 then
        return;
    end
    local sMsg = '';
    for i,v in ipairs(arg) do
        sMsg = sMsg .. tostring(v);	
    end;

    print(tostring(sMsg));
    Log(tostring(sMsg));
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
    RplCommon.print('------------------------------funcName begin--------------------------------');

    local iInitFlag	= 0;
    iInitFlag = init_getsdlval();
    RplCommon.print('---iInitFlag::' .. iInitFlag);

    if iInitFlag == 0 then
        RplCommon.print('-----------init success--------'); 

        local iRet = SorterXdr();	
        if iRet == -1 then
            return;
        end
    else
        RplCommon.print('-------init_getsdlval() failed.');
    end
    
    RplCommon.print('------------------------------funcName end--------------------------------');
    return;
end
'''

SorterXdrFunc = '''
--[[====================================================================
--函数名称：SorterXdr();
--作用：根据每条SDL话单分析归属的业务类型
--输入参数：
--输出参数：
--返回值：0
--======================================================================--]]
function SorterXdr()
    RplCommon.print('--=====================SorterXdr======================================');
    --! 获取处理标识
    local t_iTreatFlag 	= <%get_struct_value('pSubCommon',"MXdr::SSubCommon.TREAT_FLAG")%>;
    if t_iTreatFlag > 0	 then
        return 0;
    end;
    RplCommon.print('--=====================获取xdr字段值======================================');

    local t_sOutPostFix	= "";

    if  then  
        t_sOutPostFix = "";
    end

    RplCommon.print('analyse sdl.t_sOutPostFix---'..t_sOutPostFix);
    <%set_struct_value('pSubCommon', "MXdr::SSubCommon.XDR_OUT_POSTFIX", t_sOutPostFix)%>; 
    
    return 0;
end
'''

init_getsdlval_func = '''
--[[====================================================================
--函数名称：init_getsdlval()
--作用：初始化指针
--输入参数：
--输出参数：
--返回值：0--初始化成功，-1--初始化失败
--======================================================================--]]
function init_getsdlval()

    RplCommon.print('----------init_getsdlval begin-------------');
    --SCommon
    pCommon = <%get_struct_value('PXdr',"MXdr::SXdr.COMMON") %>;
    if pCommon == nil then
        RplCommon.print('--init pCommon failed.--');
        return -1;
    end	

    pSubXdr = <%get_struct_value('PXdr',"MXdr::SXdr.TOTAL_XDR") %>
    if pSubXdr == nil then
        RplCommon.print('----------init_getsdlval failed.-------------');
        return -1;
    end

    pSubCommon	= <%get_struct_value('pSubXdr',"MXdr::SSubXdr.SUB_COMMON") %>;

    pUserInfo 	= <%get_struct_value('pSubCommon',"MXdr::SSubCommon.USER_BASE_INFO") %>;

    RplCommon.print('----------init_getsdlval end-------------');
    return 0;
end
'''


fileHeader = '''-- $Id: file_name currentTime libin3 $  --
--brief:
--  
--  


require "libluabaseD";

<%use("Xdr_app.MXdr::SXdr")%>

local RplCommon={};

--0不写log，1写log
local DEBUG = 0;

--SXdr.SCommon
local pCommon       = nil;
--SXdr.SSubXdr.SSubCommon
local pSubCommon    = nil;
--
local pSubXdr       = nil;
--SXdr.SSubXdr.SSubCommon.SUserInfoBase
local pUserInfo	    = nil;

'''

#------------------------------------------------
service = sys.argv.pop()
provice = 'jx'
        
#print "============code for lua script============="        
#print

file_name = "sorter_"+service+"_"+provice+".lua"

ISOTIMEFORMAT='%Y-%m-%d %X'
curTime = time.strftime( ISOTIMEFORMAT, time.localtime() )
fileHeader = fileHeader.replace('currentTime', curTime)
fileHeader = fileHeader.replace('file_name', file_name)
print '%s'%(fileHeader)

print '%s'%(init_getsdlval_func)

print '%s'%(SorterXdrFunc)

mainFuncName = "sorter_"+service+"_main"
mainFunc = mainFunc.replace('funcName',mainFuncName)
print '%s'%(mainFunc)

print "%s"%(printFunc)



