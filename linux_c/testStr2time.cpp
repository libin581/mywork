#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>

using namespace std;

time_t str2time(const string& dt)
{
        struct tm tt;
        memset(&tt,0,sizeof(tt));
        sscanf (dt.c_str (), "%4d%2d%2d%2d%2d%2d",
                &tt.tm_year,
                &tt.tm_mon,
                &tt.tm_mday,
                &tt.tm_hour,
                &tt.tm_min,
                &tt.tm_sec);

        tt.tm_year = tt.tm_year - 1900;
        tt.tm_mon = tt.tm_mon - 1;

        //printf("tm time: %s", asctime(&tt));
        
        return mktime(&tt);
}

int main()
{
    string strStartTime="20180702173000";
    time_t tt = str2time(strStartTime);
    
    printf("%s-->%s", strStartTime.c_str(),
                ctime(&tt));
                
    time_t now;
    time(&now);
	printf("now: %ld\n", now);
	printf("%s ---> %ld\n", strStartTime.c_str(), tt);
	printf("now - starttime = %ld\n", now - tt);
    
    
    //----------------------------
    cout<<"-----------"<<endl;
    
	struct tm *local;
    local  = localtime(&now);

    printf("%04d%02d%02d%02d%02d%02d\n",
    local->tm_year+1900,
    local->tm_mon+1,
    local->tm_mday,
    local->tm_hour,
    local->tm_min,
    local->tm_sec);

    now -= 30*24*3600;
    
    local  = localtime(&now);
    printf("%04d%02d%02d%02d%02d%02d\n",
    local->tm_year+1900,
    local->tm_mon+1,
    local->tm_mday,
    local->tm_hour,
    local->tm_min,
    local->tm_sec);
    
	return 0;
}
