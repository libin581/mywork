#! /home/ut/app/perl/bin/perl 
#客户端 
use IO::Handle; 
use Socket; 
$port=8080; 
$host='127.0.0.1'; 
$packhost=inet_aton($host); 
$address=sockaddr_in($port,$packhost); 
socket(CLIENT,AF_INET,SOCK_STREAM,6); 
connect(CLIENT,$address) or die "connect to host fail\n"; 
CLIENT->autoflush(1); 
recv(CLIENT,$msg_in,20,0); 
@msg_rcv=unpack('i*',$msg_in);
print "IN:@msg_rcv\n"; 
close CLIENT; 
exit 1; 
