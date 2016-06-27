#!/usr/bin/perl -w 
# pipe1 - bidirectional communication using two pipe pairs 
# designed for the socketpair-challenged 
use IO::Handle; # thousands of lines just for autoflush :-(

pipe(PARENT_RDR, CHILD_WTR); # XXX: failure? 
pipe(CHILD_RDR, PARENT_WTR); # XXX: failure? 
CHILD_WTR->autoflush(1);  
PARENT_WTR->autoflush(1);

if ($pid = fork) { 
  #this is parent process 
  close PARENT_RDR; close PARENT_WTR; 
  print CHILD_WTR "Parent Pid $$ is sending this\n"; 
  chomp($line = <CHILD_RDR>); 
  print "Parent Pid $$ just read this: `$line'\n"; 
  close CHILD_RDR; close CHILD_WTR; 
  waitpid($pid,0); 
} 
else 
{ 
  #this is child process 
  die "cannot fork: $!" unless defined $pid; 
  close CHILD_RDR; close CHILD_WTR; 
  chomp($line = <PARENT_RDR>); 
  print "Child Pid $$ just read this: `$line'\n"; 
  print PARENT_WTR "Child Pid $$ is sending this\n"; 
  close PARENT_RDR; close PARENT_WTR; 
  exit; 
} 
