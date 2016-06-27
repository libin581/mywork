#! /bin/bash

usage(){
    echo "\
 =======usage=======
 $0 -h               : help
 $0 -a               : compile all lua scripts
 $0 file1 file2 ...  : compile file1 file2 ...
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
       fileName="*.lua"
	   shift
	   ;;
   *)
	   fileName="$fileName $1"
       shift
	   ;;
    esac
done

fileList=$(ls $fileName)
for file in $fileList; do
    if [ -f $file.lpp ]; then
	    rm $file.lpp
    fi

    if [ ! -f $file ]; then
        echo "file $file not found"
    else
        ailuac $file
        filelpp=$file.lpp
        ailua $filelpp
		echo "$file"
	fi
done

exit 0


