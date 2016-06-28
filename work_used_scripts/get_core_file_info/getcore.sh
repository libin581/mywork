#! /bin/bash
# usage: ./getcore.sh
log_path=./log
his_path=./his
ccmd=ls.cmd

IFS=$'\x0A'

if [ "$1" = "" ];then
    ddtime=`date +%Y%m%d`000000
    ddtime=`expr $ddtime - 1000000`
else 
    ddtime=$1
fi

if [ ! -d "$his_path" ]; then
    mkdir $his_path
fi
#rm $his_path/*

echo `date +%Y-%m-%d" "%H:%M:%S` "check begin, checktime is  $ddtime"
echo "host_type	   IP    core_file_num"
echo "host_type	   IP    produce_time    file_name" > $his_path/$ddtime".txt"

totalCoreNum=0
for hostlist in `cat hostxxx.info`
do 
    hostip=`echo $hostlist|awk -F ':' '{print $1}'`
    hostuser=`echo $hostlist|awk -F ':' '{print $2}'`
    hostpass=`echo $hostlist|awk -F ':' '{print $3}'`
    hosttype=`echo $hostlist|awk -F ':' '{print $4}'`
    filenum=0
    #echo $hostip checkbegin:
    ./outputsh.sh $hostip $hostuser $hostpass $ccmd
    cat $log_path/$hostip$ccmd.log | grep config/ | grep core> $log_path/$hostip$ccmd.txt
    #cat $log_path/$hostip$ccmd.txt
    for filelist in `cat $log_path/$hostip$ccmd.txt`
    do
        filetime="`echo $filelist|awk '{print $6}'`"
        filename="`echo $filelist|awk '{print $7}'`"
        #echo "filetime=$filetime"
        #echo "filename=$filename"
        if [ $filetime -ge $ddtime ] ; then # file produced today
            echo "$hosttype	$hostip	$filetime	$filename" >>  $his_path/$ddtime".txt"
            filenum=`expr $filenum + 1`
        fi 
    done
    echo "$hosttype    $hostip    $filenum"
    totalCoreNum=`expr $totalCoreNum + $filenum`
done 
echo "                     total:  $totalCoreNum"
echo `date +%Y-%m-%d" "%H:%M:%S` "check end."
