#! /bin/bash

#输出帮助信息
if [ $# -eq 0 ]
then
    echo "Usage:delete file1 [file2 file3....]"
    echo "If the options contain -f,then the script will exec 'rm' directly"
    exit 0
fi

#创建回收站目录
realrm="/bin/rm"
if [ ! -d ~/trash ]
then
    mkdir -v ~/trash
    chmod 777 ~/trash
fi

#直接删除文件
while getopts "dfiPRrvW" opt
do
    case $opt in
        f)
            exec $realrm "$@"
            exit 0
            ;;
        *)
            # do nothing     
            ;;
    esac
done

#删除大于 2G 的文件
#file_list=`ls $@`
for file in $@
do
    if [ -f "$file" ] || [ -d "$file" ]
    then
        if [ -f "$file" ] && [ `ls -l $file|awk '{print $5}'` -gt 2147483648 ]
        then
            echo "$file size is larger than 2G,will be deleted directly"
            `rm -rf $file`
            exit 0
        elif [ -d "$file" ] && [ `du -sb $file|awk '{print $1}'` -gt 2147483648 ]
        then
            echo "The directory:$file is larger than 2G,will be deleted directly"
            `rm -rf $file`
            exit 0
        fi
    fi
done
       
#移动文件到回收站并做记录
now=`date +%Y%m%d_%H_%M_%S`
filename="${file##*/}"
newfilename="${file##*/}_${now}"
mark1="."
mark2="/"
if  [ "$file" = ${file/$mark2} ]
then
    fullpath="$(pwd)/$file"
elif [ "$file" != ${file/$mark1} ]
then
    fullpath="$(pwd)${file/$mark1}"
else
    fullpath="$file"
fi	    
echo "the full path of this file is :$fullpath"
if mv -f $file ~/trash/$newfilename
then
    $(logTrashDir.sh "$newfilename $filename $now $fullpath")
    echo "files: $file is deleted"
else
    echo "the operation is failed"
fi
       
