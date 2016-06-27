#!/bin/bash
#set -x
if [ -n "$1" ] 
then
	filename="$1"
else
	echo "file name should be specified";
	echo
	echo "If you want to creat temp file, select y or n";
	read selc;

	if [ "$selc" == "y" ]
        then
		filename=temp_$(date +%m_%d_%Y)
	else
              exit 0
	fi
fi

#echo "$filename"
if [ -f "$filename" ]; then
	echo file "$filename" exists
else
	touch "$filename";echo "$filename" create successfully
fi

chmod 755 $filename

exit 0
