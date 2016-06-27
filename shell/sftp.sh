#!/bin/bash
lftp -u libin3,libin3 sftp://10.10.10.183:22 <<EOF 
cd /data01/nmjf/libin3
lcd /home/ut/work/testIssue/jx/upload/check/ftptest
get Q_hold_expr.lua
#put file.gz
by
EOF
