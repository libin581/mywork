#include <iostream>
#include <stdio.h>

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

        return mktime(&tt);
}

void main()
{
    string strStartTime="20160319115527";
    time_t tt = str2time(strStartTime);
    
    printf();
}