#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re
import pdb
from xml.etree import ElementTree

drType_serviceType={
"dr_gsm":"gsm",
"dr_addvalue":"gsm",
"dr_pbx":"gsm",
"dr_pip":"gsm",
"dr_vc":"gsm",
"dr_ip":"gsm",
"dr_pp":"gsm",
"dr_vpmn":"gsm",
"dr_poc":"gsm",
"dr_rd":"gsm",
"dr_abnor":"gsm",

"dr_wlan":"ps",
"dr_gprs":"ps",
"dr_ggprs":"ps",

"dr_sms":"sms",

"dr_ismg":"ismg",
"dr_wap":"ismg",
"dr_stm":"ismg",
"dr_ch":"ismg",
"dr_kjava":"ismg",
"dr_kj":"ismg",
"dr_lbs":"ismg",
"dr_dsp":"ismg",
"dr_cbs":"ismg",

"dr_mms":"mms",
}

drType_field={}

def parse_xml():
    xmlFilePath='/home/libin3/work/testIssue/jx/migrate/'
    xmlFile=xmlFilePath+"xdr_define.xml"
    print "start to parse file: %s"%(xmlFile)
    root = ElementTree.parse(r"%s"%(xmlFile))
    for ROW in root.findall('ROW'):
        XDR_FIELD_NAME = None
        if ROW.find("XDR_FIELD_NAME") is not None:
            XDR_FIELD_NAME = ROW.find("XDR_FIELD_NAME").text
        XDR_DR_TYPE    = None
        if ROW.find("XDR_DR_TYPE") is not None:
            XDR_DR_TYPE = ROW.find("XDR_DR_TYPE").text
        
        if XDR_DR_TYPE == None or XDR_FIELD_NAME == None:
            continue
        
        if not drType_field.has_key(XDR_DR_TYPE):
            drType_field[XDR_DR_TYPE] = []
        drType_field[XDR_DR_TYPE].append(XDR_FIELD_NAME)
    print "end to parse file: %s"%(xmlFile)
  
servieType_field_from_xml={}    

def service_field_map():
    for dr_type in drType_field.keys():
        serviceType = None
        #pdb.set_trace()
        for drType in drType_serviceType.keys():
            if dr_type == drType:
                serviceType = drType_serviceType[drType]
                break
            
        if serviceType is None:
            #print "%s is not in any service type!!!"%(dr_type)
            continue
            
        #print "%s is in %s"%(dr_type, serviceType)
            
        if not servieType_field_from_xml.has_key(serviceType):
            servieType_field_from_xml[serviceType]={}
            
        field_list = drType_field[dr_type]
        for field in field_list:
            if not servieType_field_from_xml[serviceType].has_key(field):
                servieType_field_from_xml[serviceType][field] = ""
    
  
serviceType_field_from_lua = {}    

def parse_lua_script():
    lua_serviceType = {
    "gsm":"x2s_gsm_jx.lua",
    "ismp":"x2s_ismp_jx.lua",
    "mms":"x2s_mms_jx.lua",
    "sms":"x2s_sms_jx.lua",
    "ps":"x2s_ps_jx.lua",
    }
    luaPath = "/home/libin3/work/openbilling60_cmcc/rating_billing/rating/migrate/rule/jx/"
    
    print "start to parse lua scripts"
    for service in lua_serviceType.keys():
        serviceType_field_from_lua[service]={}

        file = lua_serviceType[service]
        file = luaPath+file
        ORIG_FILE= open(file, "r")
        line = ORIG_FILE.readline()
        
        set_struct_value_line_pat = re.compile(r"<%set_struct_value.+%>")
        quote_field_pat = re.compile(r"\".+\"")
        field_pat = re.compile(r"[A-Z0-9_]+$")
        
        #setsdlval(pReserverFields,"COLLECTION_ITEM",t_sCollectionItem);
        setsdlval_line_pat = re.compile(r"setsdlval")
        #<%get_sdl_ref('pCommon', "MXdr::SCommon.ORI_CHARGE")%>
        #get_sdl_ref_pat = re.compile(r"<%get_sdl_ref.+%>")
        #pdb.set_trace()
        start_pad = re.compile(r"function set_")
        start_parse = False
        while(line):
            if start_parse == False:
                if start_pad.search(line):
                    start_parse = True
            if start_parse == False:
                line = ORIG_FILE.readline()
                continue
        
            if set_struct_value_line_pat.search(line) or \
               setsdlval_line_pat.search(line):
                quote_field_pat_search = quote_field_pat.search(line)
                if quote_field_pat_search:
                    quote_field = quote_field_pat_search.group()
                    remove_quote_field = quote_field[1:-1]
                    field_pat_search = field_pat.search(remove_quote_field)
                    if field_pat_search:
                        field = field_pat_search.group()
                        if not serviceType_field_from_lua[service].has_key(field):
                            serviceType_field_from_lua[service][field] = ""
            
            line = ORIG_FILE.readline()
        ORIG_FILE.close()
    print "end to parse lua scripts"
    
def printHelp():
    print "usage: fieldQuery.py [serviceType] [field/xls]\n\
       serviceType must be one of known service types\n\
       field can be one or more fields\n\
       xls mean fields from xdr_field_list_from_xls.py"

#-----------------------------------------------------------------------------
       
print "------------------------Segmentation line--------------------------"

service_type = {'gsm':"",'ismg':"",'mms':"",'sms':"",'ps':""}
#parse_xml()
#service_field_map()
parse_lua_script()

print "there are following services supported"
for service in service_type.keys():
    print "%s"%(service)
        
if len(sys.argv) <= 1:
    printHelp()
elif len(sys.argv) >= 2:
    serviceType = sys.argv[1]
    field_list = []
    field = sys.argv.pop()
    while(field != serviceType):
        field_list.append(field)
        field = sys.argv.pop()
    print "------------------------Segmentation line--------------------------"
    if not service_type.has_key(serviceType):
        print "service %s is not found!!!"%(serviceType)
    else:
        if len(field_list) == 0:
            print "service: %s"%(serviceType)
            for field in serviceType_field_from_lua[serviceType].keys():
                print field
            #for field in service_type[serviceType].keys():
            #    if not serviceType_field_from_lua[serviceType].has_key(field):
            #        print "[%s]"%(field)
        else:
            print "service: %s"%(serviceType)
            
            if field_list[0] == "xls":
                import xdr_field_list_from_xls
                
                field_list_from_xls = {}
                
                remove_space_pat = re.compile(r"[a-zA-Z0-9_.]+")
                field_pat = re.compile(r"[a-zA-Z0-9_]+$")
                for xdr_field in xdr_field_list_from_xls.xdr_field_list:
                    remove_space_search = remove_space_pat.search(xdr_field)
                    field = None
                    if remove_space_search:
                        remove_space_xdr_field = remove_space_search.group()
                        field_search = field_pat.search(remove_space_xdr_field)
                        if field_search:
                            field = field_search.group()
                            
                    if field is None:
                        print "%s is not correct format!!!"%(xdr_field)
                    else:
                        field_list_from_xls[field] = ""
                    
                for field in serviceType_field_from_lua[serviceType].keys():
                    if field_list_from_xls.has_key(field):
                        print "%s"%(field)
                    else:
                        print "%s is in service %s, but not included in xls!!!"%(field, serviceType)
                
                print "------------------------Segmentation line--------------------------"
                
                for field in field_list_from_xls.keys():
                    if not serviceType_field_from_lua[serviceType].has_key(field):
                        print "%s is in xls, but not included in service %s!!!"%(field, serviceType)
            
            else:
                for field in field_list:
                    if serviceType_field_from_lua[serviceType].has_key(field):
                        print "%s"%(field)
                    elif service_type[serviceType].has_key(field):
                        print "[%s]"%(field)
                    else:
                        print "%s is not in service %s"%(field, serviceType)


    
    
