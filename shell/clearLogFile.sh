#! /bin/sh
keyWord=log
fileList=$(ls $keyWord*)
if [ fileList == "" ]; then
	echo "the file has been clear"
else
	for file in $fileList; do
	    echo "delete $file"
	    rm -rf $file
	done
fi
exit 0