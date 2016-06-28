#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re
import pdb

drType_serviceType={
"dr_gsm":"cs",
"dr_addvalue":"cs",
"dr_pbx":"cs",
"dr_pip":"cs",
"dr_vc":"cs",
"dr_ip":"cs",
"dr_pp":"cs",
"dr_vpmn":"cs",
"dr_poc":"cs",
"dr_rd":"cs",
"dr_abnor":"cs",

"dr_wlan":"ps",
"dr_gprs":"ps",
"dr_ggprs":"ps",

"dr_sms":"sms",

"dr_ismg":"ismp",
"dr_wap":"ismp",
"dr_stm":"ismp",
"dr_ch":"ismp",
"dr_kjava":"ismp",
"dr_kj":"ismp",
"dr_lbs":"ismp",
"dr_dsp":"ismp",
"dr_cbs":"ismp",
"dr_mms":"ismp",
}

print "drType         |   service"
print "--------------------------"
for drType in drType_serviceType.keys():
    print "%-15s<---->%10s"%(drType, drType_serviceType[drType])

for drType in drType_serviceType.keys():
	print "m_xdrType2ServiceType.insert(\""+ \
	      drType+\
	      "\",\""+\
		  drType_serviceType[drType]+\
		  "\");"
