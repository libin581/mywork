//compile it use the following command
//g++ hello.cc hello.pb.cc -o hello -I/usr/local/protobuf/include -L/usr/local/lib -lprotobuf
#include <stdio.h>
#include <string.h>

#include "hello.pb.h"

using namespace std;
using namespace hello;

int main()
{
    Hello a;
    a.set_id(101);
    a.set_name("huangwei");

    string tmp;
    bool ret = a.SerializeToString(&tmp);
    if (ret) 
    {
        printf("encode success!\n");
    }
    else 
    {
        printf("encode faild!\n");
    }

    char chBuf[100];
    strcpy(chBuf, tmp.c_str());
    string tmp2 = chBuf;


    Hello b;

    ret = b.ParseFromString(tmp2);
    if (ret)
    {
        printf("decode success!\n id= %d \n name = %s\n", b.id(), b.name().c_str());
    }
    else
    {
        printf("decode faild!\n");
    }

    return 0;
}


