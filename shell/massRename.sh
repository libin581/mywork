#! /bin/bash
keyWord=".bak"
fileList=$(ls *$keyWord*)
if [ fileList == "" ]; then
	echo "there is no file named $keyWord"
else
	for file in $fileList; do
	    echo $file
		#expr index "$keyWord" t
		strLen=${#file}
		newName=${file:0:strLen-4}
	    echo "rename $file to $newName"
	    mv $file $newName
	done
fi
