#! /usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import os
import sys
import pdb

province= "jiangxi"

print "province:%s"%(province)

#========template migrate from 4.0 to 6.0
sys.argv = ["decode_template_migrate.py",province]
execfile("decode_template_migrate.py")

#========minimal modify
sys.argv = ["decode_template_mini_modify.py",province]
execfile("decode_template_mini_modify.py")


#============================================
#format pretty
#sys.argv = ["format_pretty.py",province]
#execfile("format_pretty.py")

#========statistic
#sys.argv = ["decode_template_statistics.py",province]
#execfile("decode_template_statistic.py")

#======特殊处理=====
#sys.argv = ["decode_template_statistics.py",province]
#execfile("decode_template_specProcess.py")



