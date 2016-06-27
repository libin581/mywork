#/bin/bash

namemax=""
max=0
function scandir() {   
    local cur_dir parent_dir workdir   
	workdir=$1   
    cd ${workdir}  
		 
    if [ ${workdir} = "/" ]   
    then   
        cur_dir=""   
    else   
        cur_dir=$(pwd)   
    fi   

    for dirlist in $(ls ${cur_dir})   
    do   
        if test -d ${dirlist}
        then   
	        cd ${dirlist}   
	        scandir ${cur_dir}/${dirlist}   
	        cd ..   
	    else   
			name=${cur_dir}/${dirlist}
			echo $name
			
            size=$(ls -l $name | awk '{print $5}')
            if [ $size -ge $max ]; then
                max=$size
                namemax=$name
            fi
	    fi   
	done   
}  

scandir $1
echo
echo "the max file is $namemax"

