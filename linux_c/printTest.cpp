#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <unistd.h>

int main()
{
    char str[10]={0};
    int nLen=snprintf(str,sizeof(str),"%-4s","12");
    //int nLen=sprintf(str,"%0*d%s",4-strlen("12"),0,"12");
    printf("str=%s\n",str);
    printf("nLen=%d\n",nLen);

    while(1){
	    fprintf(stderr, "*");//与stdout不同的是， stderr没有经过缓冲处理；输出到stderr的数据会直接被发送到终端
	    sleep(1);
		printf(".");
		fflush(stdout);//显式地刷新输出流
		sleep(1);
        printf("+");
		}


    return 0;
}
