#! /bin/bash

filename=$1

OLD_IFS="$IFS" 
IFS="/" 
arr=($filename) 
IFS="$OLD_IFS" 
#for s in ${arr[@]} 
#do 
#    echo "$s" 
#done
length=${#arr[@]}
filename=${arr[length-1]}

#获取相应记录
originalPath=$(awk /$filename/'{print $4}' "$HOME/trash/.log")

#查找原文件名及现文件名字段
filenameNow=$(awk /$filename/'{print $1}' ~/trash/.log)
filenamebefore=$(awk /$filename/'{print $2}' ~/trash/.log)
echo "you are about to restore $filenameNow,original name is $filenamebefore"
echo "original path is $originalPath"

#恢复文件到原来位置并删除相应记录
echo "Are you sure to do that?[Y/N]"
read reply
if [ $reply = "y" ] || [ $reply = "Y" ]
then
    $(mv -b "$HOME/trash/$filename" "$originalPath")
    $(sed -i /$filename/'d' "$HOME/trash/.log")
else
    echo "no files restored"
fi

