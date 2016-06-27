#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <sys/time.h> 
#include <time.h>

typedef long  long     int64;
typedef int            int32;

int64 time2loc(int64 ullTimet);

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
       printf("%s----> %lld\n", argv[1], time2loc(ullTimet));   
    }
}

int64 time2loc(int64 ullTimet)    // 0.002 ms
{
    struct tm timeinfo;
    int64 llTemp = ullTimet;
    int32 iSec = llTemp%100;//得到秒
    llTemp /= 100;
    int32 iMin = llTemp%100;
    llTemp /= 100;
    int32 iHour = llTemp%100;
    llTemp /= 100;
    int32 iDay = llTemp%100;
    llTemp /= 100;
    int32 iMon = llTemp%100;
    llTemp /= 100;
    int32 iYear = llTemp%10000;

    timeinfo.tm_year = iYear;
  	timeinfo.tm_mon = iMon;
  	timeinfo.tm_mday = iDay;
  	timeinfo.tm_hour = iHour;
  	timeinfo.tm_min = iMin;
  	timeinfo.tm_sec = iSec;

	//时间做调整
	timeinfo.tm_year -= 1900;
	timeinfo.tm_mon -= 1;
    
	ullTimet = mktime(&timeinfo);

    return ullTimet;
}