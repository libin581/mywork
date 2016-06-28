#! /usr/bin/python
# -*- coding: utf-8 -*-
 
import time
import sys
import pdb
import string
import re

fileHeader = '''-- $Id: fileName commitTime libin3 $  --
require "libluabaseD";
<% use("Xdr_app.MXdr::SXdr") %>

do
	t_iResult	= 0;
    
	pHeadRecord	= "";
	pBodyRecord	= "";
	pTailRecord	= "";
	pOutFileName	= "";
    
	t_lBeginTime	= 20301231000000;
	t_lEndTime	= 20110101000000;

	t_iValidNumber	= 0;
	t_iRoamFee	= 0;
	t_iTotalLFee1	= 0;
	t_iForwardBasicFee	= 0;
	t_iTotalFee	= 0;
	
	t_iLaterOnceNumber	 = 0;
	t_iErrLaterOnce	= 0;
	t_iErrLater	= 0;
	t_sErrorCode 	= "";
    
    t_iDebug = 1;
end
'''

reset_val_func = '''
--[[============================================================================
--函数名称: reset_val
--作    用: 重新初始化统计变量
--输入参数:
--输出参数:
--返回值：
--==========================================================================--]]
local function reset_val()
	print('----------reset_val begin-------------');
	t_iResult	= 0;
    
	pHeadRecord	= "";
	pBodyRecord	= "";
	pTailRecord	= "";
	pOutFileName = "";

	t_lBeginTime = 20301231000000;
	t_lEndTime	= 20110101000000;

	t_iValidNumber	= 0;
	t_iRoamFee	= 0;
	t_iTotalLFee1	= 0;
	t_iForwardBasicFee	= 0;
	t_iTotalFee	= 0;
	
	t_iLaterOnceNumber	 = 0;
	t_iErrLaterOnce	= 0;
	t_iErrLater	= 0;
	t_sErrorCode 	= "";

	print('----------reset_val end-------------');
	return 0;
end
'''

dealXdr_func = '''
----[[============================================================================
----函数名称: dealXdr
----作    用: 逐条处理详单
----输入参数:
----输出参数:
----返回值：
----==========================================================================--]]
local function dealXdr()
    print_new("--------- dealXdr begin ----------------");	

    local	iRet = -1;
	local	t_sErrorCode = "";

    
	t_iResult	= 1;
	
	print_new("--------- dealXdr end. ----------------");
	
	return 0;
end
'''

getHeadRecord_func = '''
local function getHeadRecord()
	print_new("--------- getHeadRecord begin ----------------");
	
	local   iRet = -1;

	local	sProvCode	= CONST_PROV_CODE;
	local	sProcNo		= CONST_PROC_NO;
	local	t_sEmpty	= " ";
	local sCurTime = "";
	iRet, sCurTime =  GetPTime();
	local	sHeadFileDate		= CONST_FILE_DATE;
	if sProcNo == "0" then 
		sCurTime	= sHeadFileDate.."000000";
	else
		sCurTime	= sHeadFileDate..string.sub(sCurTime,9,14);
	end
    
	pHeadRecord = ;
	
	print_new("--------- getHeadRecord end. ----------------");
	
	return 0;
end
'''

getTailRecord_func = '''
local function getTailRecord()
	print_new("--------- getTailRecord begin ----------------");
	
	local   iRet = -1;

	local sCurTime = "";
	iRet, sCurTime =  GetPTime();
	print_new("-- PT time ::" .. sCurTime);

	local	t_sEmpty = " ";
	local	sProvCode	= CONST_PROV_CODE;
	local	sProcNo		= CONST_PROC_NO;
	t_iRoamFee		= math.floor((t_iRoamFee + 5)/10);
	t_iTotalLFee1		= math.floor((t_iTotalLFee1 + 5)/10);
	t_iForwardBasicFee	= math.floor((t_iForwardBasicFee + 5)/10);
	t_iTotalFee		= math.floor((t_iTotalFee + 5)/10);

	pTailRecord =  ;

	print_new("--------- getTailRecord end. ----------------");

	return 0;
end;
'''

getFileName_func = '''
local function getFileName()
	print_new("--------- getFileName begin ----------------");

	reset_val(); --重新初始化
	local   iRet = -1;

	local	sProvCode	= CONST_PROV_CODE;
	local	sProcNo		= CONST_PROC_NO;
	local	sFileType	= CONST_FILE_TYPE;
	local	sFileDate	= CONST_FILE_DATE;

    --VMMSYYYYMMDDNNN.ZZZ "NNN"表示当日文件编号 "ZZZ"表示上/下发文件的公司
	pOutFileName = sFileType
		.. sFileDate
		.. lpad(sProcNo,"0",3)
		.. "."
		.. (sProvCode); 
    
	print_new("--------- getFileName end. ----------------");

	return 0;
end;
'''

main_func = '''    
function roamin_service_main()
	print_new('-----roamin_service_main begin---');
	
	local	iRecordFlag = CONST_RECORD_FLAG;
	local	iRet = 0;
	
	print_new("--------- RecordFlag ::" .. iRecordFlag);	
	
	if iRecordFlag == 1 then
		iRet = dealXdr();	-- body record
		if iRet == -1 then
			return;
		end;
	elseif iRecordFlag == 0 then
		iRet = getHeadRecord(); -- head record 
		if iRet == -1 then
			return;
		end;
	elseif iRecordFlag == 2 then
		iRet = getTailRecord(); -- tail record
		if iRet == -1 then
			return;
		end;
	elseif iRecordFlag == 3 then
		iRet = getFileName(); -- get filename
		if iRet == -1 then
			return;
		end;
	end;

    print_new('-----roamin_service_main end----');

	return;
end;
'''

print_func = '''
--============================================================================
--函数名称: print
--作    用: 输出信息到屏幕和日志文件
--输入参数: 日志信息
--输出参数: 无
--返回值：无
--============================================================================
function print_new(...)
	local sMsg = '';
	for i,v in ipairs(arg) do
		sMsg = sMsg .. tostring(v);	
	end;
    
    if t_iDebug == 1 then
        print(tostring(sMsg));
        LogAppend(tostring(sMsg));
    end
end;
'''
    
    
#------------------------------------------------
service = sys.argv.pop()
fileName = "upf_"+service+"_jx.lua"
fileHeader = fileHeader.replace("fileName", fileName)
ISOTIMEFORMAT='%Y-%m-%d %X'
curTime = time.strftime( ISOTIMEFORMAT, time.localtime() )
fileHeader = fileHeader.replace("commitTime", curTime)

main_func = main_func.replace("service", service)

print fileHeader
print 
print reset_val_func
print
print dealXdr_func
print
print getHeadRecord_func
print 
print getTailRecord_func
print 
print getFileName_func
print 
print main_func
print
print print_func
print


