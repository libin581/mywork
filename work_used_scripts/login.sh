#! /bin/bash

echo "  decode: 60-69"
echo "  jfzw:   16-33"
echo "  mdb:    4-15"
echo "  roam:   360-369"
#echo "  file_trans:     billsynt 675\677,       billdist 775\777"
echo "  online inbossd:    40-49"
echo "  online revRating:    50-59"
echo "  SRM:    305\307\309"
echo "  hangzhou: 183"
echo "please input a num for you login machine"

read  num

IP=$num

PassWd1="Ailk@4$IP"
PassWd2="Ailk@14$IP"
PassWd3="libin3"
passwd4="zc_public"
passwd5="nmbilldevcs"

if [ $num -ge 60 -a  $num -le 69 ]; then
echo "ssh billapp@10.180.214.$IP"
echo "PassWord:$PassWd1"
expect $HOME/work/scripts/login.exp $PassWd1  10.180.214.$IP billapp
fi

if [ $num -ge 16 -a $num -le 33 ]; then
echo "ssh billapp@10.180.214.$IP"
echo "PassWord:$PassWd1"
expect $HOME/work/scripts/login.exp $PassWd1  10.180.214.$IP billapp
fi

if [ $num -ge 4 -a $num -le 9 ]; then
echo "ssh billmdb@10.180.214.$IP"
echo "PassWord:$PassWd2"
expect $HOME/work/scripts/login.exp $PassWd2  10.180.214.$IP billmdb
fi

if [ $num -ge 10 -a $num -le 15 ]; then
echo "ssh billmdb@10.180.214.$IP"
echo "PassWord:$PassWd1"
expect $HOME/work/scripts/login.exp $PassWd1  10.180.214.$IP billmdb
fi

if [ $num -ge 40 -a $num -le 49 ]; then
echo "ssh billapp@10.180.214.$IP"
echo "PassWord:$PassWd1"
expect $HOME/work/scripts/login.exp $PassWd1  10.180.214.$IP billapp
fi

if [ $num -ge 50 -a $num -le 59 ]; then
echo "ssh billapp@10.180.214.$IP"
echo "PassWord:$PassWd1"
expect $HOME/work/scripts/login.exp $PassWd1  10.180.214.$IP billapp
fi

if [ $num -ge 360 -a  $num -le 369 ]; then
IP=`expr $num - 300`
echo "ssh billroam@10.180.214.$IP"
echo "PassWord:Ailk@4$IP"
expect $HOME/work/scripts/login.exp Ailk@4$IP  10.180.214.$IP billroam
fi

if [ $num -eq 305 -o $num -eq 307 -o $num -eq 309 ]; then
IP=`expr $num - 300`
echo "ssh billsrm@10.180.214.$IP"
echo "PassWord:Ailk@14$IP"
expect $HOME/work/scripts/login.exp Ailk@14$IP  10.180.214.$IP billsrm
fi

if [ $num -eq 183 ]; then
echo "select the user: libin3/zc_public/nmbilldevcs"
read user
echo "ssh $user@10.10.10.183"
echo "PassWord:$user"
expect $HOME/work/scripts/login.exp $user  10.10.10.183 $user
fi

echo "Good Bye!"
