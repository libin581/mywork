#! /bin/bash

usage(){
    echo "\
 =======usage=======
 $0 -h               : help
 $0 process_id       : eg. $0 30657
 
 default:
 times    = 20
 interval = 30(s)
"
}

if [ $# -eq 0 ]; then
    usage
	exit 0
fi

process_id=""
case $1 in
-h)
   usage
   exit 0
   ;;
*)
   process_id=$1
   ;;
esac

times=20
interval=30
ipAddr=ifconfig |grep -Po '(?<=addr:).*(?=Bc)'
resFile=$ipAddr"pstack_"$process_id".txt"
for((i=1;i<=$times;i++));do 
    #echo $SHELL;
    pstack $process_id | tee -a $resFile
    sleep $interval
done

#pstack 30657


