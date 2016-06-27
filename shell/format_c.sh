#!/bin/bash

usage(){
    echo "\
 =======usage=======
 $0 -h                     : help
 $0 -a                     : format all c/c++/h/hpp files
 $0 file1 file2 ...          : compile file1 file2 ...
"
}

if [ $# -eq 0 ]; then
    usage
	exit 0
fi

fileName=""
while [ $# -gt 0 ]
do
   echo "..$1"
   case $1 in
   -h)
       usage
	   exit 0
	   ;;
   -a)
       fileName="*.c *.cpp *.h *.hpp "
	   shift
	   ;;
   *)
	   fileName="$fileName $1"
       shift
	   ;;
    esac
done

alias astyle='astyle --style=ansi --mode=c -s4 -S -N -L -m0 -M40 --convert-tabs --suffix=.pre'

fileList=$(ls $fileName)
for file in $fileList; do
    if [ ! -f $file ]; then
        echo "file $file not found"
    else
        astyle $file
		#echo "$file"
		if [ -f $file.orig ]; then
           rm $file.orig
		fi
	fi
done

exit 0



#astyle *.h *.cpp --style=ansi --mode=c -s4 -S -N -L -m0 -M40 --convert-tabs --suffix=.pre

