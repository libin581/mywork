#! /bin/bash
#outputsh.sh 10.182.11.13 nbngmdb Bi_15sJF ls.cmd
realsh_path=./realsh
log_path=./log
fcmd=$4

if [ ! -d $realsh_path ]  ;then 
    mkdir $realsh_path
fi
#rm $realsh_path/*

outsh=$realsh_path/$1$4.sh

if [ ! -d $log_path ]  ;then 
    mkdir $log_path
fi
#rm $log_path/*

echo "#! /usr/bin/expect -f" > $outsh
echo "set host_ip $1" >> $outsh
echo "set username $2" >> $outsh
echo "set passwd $3">> $outsh
echo "set timeout -1">> $outsh
echo "spawn ssh \$username@\$host_ip " >> $outsh
echo "expect {" >> $outsh
echo "\"yes/no\" { send \"yes\r\"; exp_continue}" >> $outsh
echo "\"password:\" { send \"\$passwd\r\" } " >> $outsh
echo "}" >> $outsh
echo "sleep 1 " >> $outsh
if [ "$fcmd" == "" ]; then
    echo interact >> $outsh
else
    if [ ! -f "$fcmd" ]; then 
        echo interact >> $outsh
    else
        IFS=$'\x0A'
        #echo $fcmd
        for strcmd in `cat $fcmd`
        do
            #echo "$strcmd"
            echo "send \""$strcmd" \\r\"" >> $outsh
            echo "sleep 1 " >> $outsh
        done 
    fi
fi
echo "send \"exit\r\" ">> $outsh
echo interact >> $outsh
chmod +x $outsh
$outsh >$log_path/$1$4.log
