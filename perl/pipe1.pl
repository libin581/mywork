#!/usr/bin/perl -w
my $uid ="test 123";

pipe(CHILD_RDR, PARENT_WTR);
my $pid = fork();
if ($pid != 0) {
#this is parent process
close CHILD_RDR;
print PARENT_WTR "$uid";
} else {
# this is the child process
close PARENT_WTR;
$u = <CHILD_RDR>; 
print $u;

}
