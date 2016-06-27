#! /bin/bash

if  [ 1 -gt $# ];then
	echo "please input filename"
	exit 1
fi

cfilename=$1

if [ ! -f $cfilename ]; then
	echo "file \"$cfilename\" not exist!!"
	exit 1
fi

objfilename=$cfilename".o"

echo $cfilename | grep -e "\.cpp" > /dev/null
if [ $? -eq 0 ]; then
    g++ -o $objfilename $cfilename
    ls $cfilename*
	echo "--------------------------------"
	./$objfilename
    exit 1
fi

echo $cfilename | grep -e "\.c" > /dev/null
if [ $? -eq 0 ]; then
    gcc -o $objfilename $cfilename
    ls $cfilename*
	echo "--------------------------------"
	./$objfilename
    exit 0
fi


echo "not recognize file format: $cfilename"


