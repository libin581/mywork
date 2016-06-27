#! /bin/bash
ftp -n<<!
open 10.10.10.183
user libin3 libin3
binary
cd /data01/nmjf/libin3
lcd /home/ut/work/testIssue/jx/upload/check/ftptest
get Q_hold_expr.lua
close
bye
!

#this script can't use
