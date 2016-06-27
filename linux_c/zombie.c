#include <stdlib.h> 
#include <sys/types.h> 
#include <unistd.h> 
 
 int main () 
 { 
    pid_t child_pid; 
	 
   /* 创建一个子进程 */ 
     child_pid = fork (); 
   if (child_pid > 0) { 
    /*这是父进程。休眠一分钟。 */ 
      sleep (60); 
    } 
   else { 
       /*这是子进程。立刻退出。become zombie process */ 
      exit (0); 
    } 
   return 0; 
} 
