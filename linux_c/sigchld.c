#include <signal.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

sig_atomic_t child_exit_status;

void clean_up_child_process (int signal_number)
{
    /* 清理子进程。*/
    int status;
    wait (&status);
    /* 在全局变量中存储子进程的退出代码。*/
    child_exit_status = status;
    if (WIFEXITED(status))
        printf("child exited with code %d\n",
               WEXITSTATUS(status));
}

int main ()
{
    /* 用 clean_up_child_process 函数处理 SIGCHLD。*/
    struct sigaction sigchild_action;
    memset (&sigchild_action, 0, sizeof (sigchild_action));
    sigchild_action.sa_handler = &clean_up_child_process;
    sigaction (SIGCHLD, &sigchild_action, NULL);

    /* 现在进行其它工作，包括创建一个子进程。*/
    printf("fork program starting\n");

    pid_t pid;
    char *message;
    int n;
    int exit_code;

    pid = fork();

    switch (pid)
    {
    case -1:
        perror("fork failed");
        exit(1);
    case 0:
        message = "This is the child";
        n = 3;
        exit_code  = 37;
        break;
    default:
        message = "This is the parent";
        n = 6;
        exit_code = 0;
        break;
    }


    for (; n>0; n--)
    {
        puts(message);
        sleep(1);
    }

    exit(exit_code);
    return 0;
}




