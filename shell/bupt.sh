#!/bin/bash
# 在下面的username中填入你自己的学号
# 在password中输入你的密码
username=school_id
password=PASSWD

URL_LOGIN=http://gw.bupt.edu.cn
URL_LOGOUT=http://gw.bupt.edu.cn/F.htm

login()
{
     RESULT=`curl -s -d "DDDDD=$username&upass=$password&0MKKey=123456" "$URL_LOGIN"`
     echo login OK!
     IP=`curl -s "$URL_LOGIN" | grep ^time`
     IP1=$(echo $IP | cut -d ' ' -f 1 | cut -d "'" -f 2) 
     echo -n -e "已使用时间 Used time :" $IP1 "Min\n" 
     IP2=$(echo $IP | cut -d ' ' -f 2 | cut -d "'" -f 3) 
#     echo $IP2
     echo -n -e "已使用校外流量 Used internet traffic :" $IP2 "KByte\n" 
}

logout()
{     
#      echo logout
      RESULT=`curl -s "$URL_LOGOUT"`
      echo logout!
} 

usage()
{	
echo "Usage: $0 [-i|-o] "
	echo "where:     -i login to bupt school network"
	echo "           -o logout from bupt school network"
	echo 
	exit
}


case $1 in
-i)
      login;;
-o)

      logout;;
*)
      usage;;
esac
