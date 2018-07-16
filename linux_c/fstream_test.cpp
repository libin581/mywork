#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

ofstream outfile;

char pTestFile[] = "/home/ut/study/mywork/linux_c/fstream.txt";

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

void readLog(){
	std::string xdr_data;
	std::ifstream file(pTestFile, std::fstream::binary);
	if (file)
	{
		file.seekg (0, file.end);
		int length = file.tellg();
		file.seekg (0, file.beg);
		
		xdr_data.reserve(length);
		
		int pos;
		char buffer[10];
		for(pos=0; pos<length&&file;pos+=10)
		{
			int step = (length-pos)>10?10:(length-pos);
			file.read (buffer, step);
			xdr_data.append(buffer, step);
		}
		printf("read file as follows:%s\n",xdr_data.c_str());
	}
	file.close();
}

int main(int argc, char* argv[])
{
    printf("-----write fstream.txt begin-----\n");
    writeLog();
    writeLog2();
    printf("-----write fstream.txt end-----\n");
    
    printf("\n\n");
    
    printf("-----read fstream.txt begin-----\n");
    readLog();
    printf("-----read fstream.txt end-----\n");
    return 0;
}
