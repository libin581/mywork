#!/bin/bash
lftp -u libin3,libin3 sftp://10.10.10.183:22 <<EOF 
cd /data01/nmjf/libin3/test
lcd /home/ut/share/mywork/shell
mget *.lua
#put file.gz
by
EOF
