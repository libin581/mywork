#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

ofstream outfile;

char pTestFile[] = "/home/ut/study/mywork/linux_c/ofstream.txt";

void writeLog()
{
    outfile.open(pTestFile, ios::app);
    if (!outfile) //检查文件是否正常打开//不是用于检查文件是否存在
    {
        cout<<pTestFile<<" can't open 1"<<endl;
        abort(); //打开失败，结束程序
    }
    else
    {
        outfile << "world" << endl;
        outfile.close();
    }
}
void writeLog2()
{
    outfile.open(pTestFile, ios::app);
    if (!outfile) //检查文件是否正常打开
    {
        cout<< pTestFile<< " can't open 2"<< endl;
        abort(); //打开失败，结束程序
    }
    else
    {
        outfile << "Write log2" << endl;
        outfile.close();
    }
}
int main(int argc, char* argv[])
{
    writeLog();
    writeLog2();
    printf("Hello World!\n");
    return 0;
}
