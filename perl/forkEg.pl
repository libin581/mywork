#!usr/bin/perl -w 
$pid=fork();
die "Error:$!\n" unless defined $pid;  #制定程序的错误机制，此步可略

if($pid!=0){   #条件选择，测试$pid值，以确定为子进程还是父进程
  print"This is a main pid!PID is $$!\n"; #$pid值不等于0，此为父进程(附:$$为保留变量，其值为此进程的PID) 
}else{   #否则..... 
  print"This is a sub pid!PID is $$!\n";  #$pid值为0，此为子进程 
} 
exit 1;
