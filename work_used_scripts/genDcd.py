#! /usr/bin/python

import subprocess
import os
import shutil
import sys
import re
import pdb

import fields as field_list

space_head_pat=re.compile(r"^\s+")
space_tail_pat=re.compile(r"\s+$")
def remove_space_head_tail(field):
    field=space_head_pat.sub("", field)
    field=space_tail_pat.sub("", field)
    return field

for i, field in enumerate(field_list.field_list):
    field=remove_space_head_tail(field)
    field_name = "gsm"+str(i)
    field_next_field = "gsm"+str(i+1)
    if i == 0:
        field_name = "BEGIN"
    
    print "FIELD //%s"%(field)
    print "{"
    print "    FIELD_NAME = %s"%(field_name)
    print "    FIELD_LEAF = YES"
    print "    FIELD_NEXT_FIELD = %s"%(field_next_field)
    print "    FIELD_XDRKEY = %s"%(field)
    print "    DECODE"
    print "    {"
    print "        DECODE_FUNC_TYPE = decode_asc"
    print "        DECODE_SPLIT = ;"
    print "    }"
    print "}"
