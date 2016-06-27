#! /home/ut/app/perl/bin/perl 
#服务端 
use IO::Handle; 
use Socket; 
$port=8080; 
$host='127.0.0.1'; 
$packhost=inet_aton($host); 
$address=sockaddr_in($port,$packhost); 
socket(SERVER,AF_INET,SOCK_STREAM,getprotobyname('tcp')); 
bind(SERVER,$address); 
listen(SERVER,10); 
while(1){ 
next unless (accept(CLIENT,SERVER)); 
CLIENT->autoflush(1); 
print "\n++++++++++++\n";
#$msg_out="WHAT DO YOU WANT?\n"; 
$msg_out=pack("i*", 1,2,3,4,5,6);
send(CLIENT,$msg_out,0); 
close CLIENT; 
close SERVER; 
exit 1;
}
