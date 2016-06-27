#! /bin/bash

usage(){
    echo "\
 =======usage:replace oldstring with newstring =======
 use: $0 oldstring newstring
 default to replace all files in current path.
"
}

if [ $# -lt 2 ]; then
    usage
	exit 0
fi

oldString="$1"
newString="$2"
path="./"
if [ "$3" != "" ]; then
	path="$3"
fi

fileList=`grep $oldString -rl $path`

echo replace $oldString with $newString
echo file:$fileList

sed -i "s/$oldString/$newString/g" $fileList #`grep $oldString -rl $path`

exit 0
