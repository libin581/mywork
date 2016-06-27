#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <sys/time.h> 
#include <time.h>

typedef long  long     int64;
typedef int            int32;

int64 time2ll(int64 llTime);

int32 main(int argc, char** argv)
{
    if (argc == 1) {
        fprintf(stderr, "no time input\n");
        exit(EXIT_FAILURE);
    }
    else
    {
       int64 ullTimet = atoll(argv[1]);
       //printf ("%lld\n", ullTimet);
       printf("%s----> %lld\n", argv[1], time2ll(ullTimet));   
    }
}

int64 time2ll(int64 llTime)
{     
    struct tm t = {0};  
    gmtime_r((const time_t *)&llTime, &t);
    
    char szBuf[64] = {0};   
    //小时+8，是因为弥补0时区
    snprintf(szBuf, sizeof(szBuf) - 1, "%04d%02d%02d%02d%02d%02d",          
        t.tm_year + 1900, t.tm_mon + 1, t.tm_mday, t.tm_hour + 8, t.tm_min, t.tm_sec); 
    //printf("%d,%d,%d,%d,%d,%d\n",  t.tm_year + 1900, t.tm_mon + 1, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec);
    int64 llRet = atoll(szBuf); 

    return llRet;
}