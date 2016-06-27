#! /bin/bash
path=`pwd`
for file in `ls $path/*nm.lua`
do
    newfile=`echo $file | sed 's/nm/jx/'`
	echo "$file ----> $newfile"
    mv $file $newfile
done
