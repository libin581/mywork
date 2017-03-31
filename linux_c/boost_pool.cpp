//开源C++函数库Boost内存池使用与测试
//http://tech.it168.com/a2011/0726/1223/000001223399_all.shtml

//#include "stdafx.h"
#include <iostream>
#include <ctime>
#include <vector>
#include <boost/pool/pool.hpp>
#include <boost/pool/object_pool.hpp>
using namespace std;
using namespace boost;

const int MAXLENGTH = 1000000;

int main ( )
{
    boost::pool<> p(sizeof(int));
    int* vec1[MAXLENGTH];
    int* vec2[MAXLENGTH];

    clock_t clock_begin = clock();
    for (int i = 0; i < MAXLENGTH; ++i)
    {
        vec1[i] = static_cast<int*>(p.malloc());
    }
    for (int i = 0; i < MAXLENGTH; ++i)
    {
        p.free(vec1[i]);
        vec1[i] = NULL;
    }

    clock_t clock_end = clock();
    cout<<"pool programe run "<<clock_end-clock_begin<<" system clock"<<endl;

    clock_begin = clock();
    for (int i = 0; i < MAXLENGTH; ++i)
    {
        vec2[i] = new int;
    }
    for (int i = 0; i < MAXLENGTH; ++i)
    {
        delete vec2[i];
        vec2[i] = NULL;
    }

    clock_end = clock();
    cout<<"new programe run "<<clock_end-clock_begin<<" system clock"<<endl;

    return 0;
}
