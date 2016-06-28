#! /bin/bash

times=1000
interval=600

for((i=1;i<=$times;i++));do 
    resFile="get_core_$i.txt"
    ./getcore.sh | tee $resFile
    sleep $interval
done

#pstack 30657
