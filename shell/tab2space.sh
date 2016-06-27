#! /bin/sh

usage(){
    echo "\
 =======usage=======
 $0 -h               : help
 $0 -a               : convert all files
 $0 file1 file2 ...  : convert file1 file2 ...
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
       fileName="*"
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

    if [ ! -f $file ]; then
        echo "file $file not found"
    else
        expand -t 4 $file > $file~
       	rm $file
        mv $file~ $file
        echo "$file"
 
	fi
done

exit 0


