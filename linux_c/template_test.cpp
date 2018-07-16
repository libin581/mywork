#include <iostream>

using namespace std;

template <typename T>
T add_t(const T &v1, const T &v2)
{
    return v1+v2;
}

const int SIZE=8;
template <class T>
class Smemory { //定义类模板Smemory
    T data[SIZE]; //类型为T，长度为SIZE的数组data[]为数据成员
    int count;
public:
    Smemory( ){ count=0; }
    void mput(T x); //mput()函数的参数x的类型是T
    T mget( ); //声明返回值类型为T的成员函数mget()
};
template <class T>
void Smemory<T>::mput(T x) //定义成员函数mput()，函数的参数类型为T,该函数用于为数据成员　data数组的各个元素赋值
{
    if(count==8) { cout<<"Memory is full"; return; }
    data[count]=x;
    count++;
}

template <class T>
T Smemory<T>::mget( )//定义成员函数mget()，函数的返回类型为T，该函数用于取出数据成员　data数组的各个元素
{
    if(count==0) { cout<<"Memory is empty"; return 0; }
    count--;
    return data[count];
}

//=========get from tap3 code begin==========

typedef struct OperInfo_s{
    int tenant_id;
} OperInfo;

class LoadOperInfo{
public:
	LoadOperInfo()
	{
	}
	void operator () (OperInfo& oper_info); //重载()

};

void LoadOperInfo::operator () (OperInfo& oper_info)
{
	cout<<"oper_info.tenant_id = "<<oper_info.tenant_id<<endl;
}

void process(OperInfo oper_info)
{
    cout<<"oper_info.tenant_id = "<<oper_info.tenant_id<<endl;
}

template <typename Handler>
int foreach_OperInfo(Handler handler)
{	
    OperInfo oper_info;
    oper_info.tenant_id = 102;
	handler(oper_info);

	return 0;
}
//=========get from tap3 code end==========


int main( )
{
    int a=3, b=5;
    cout<<"a+b="<<add_t(a,b)<<endl;

    Smemory<int> mo1;
    int i; char ch='A';//将Smemory实例化，并创建对象mo1
    Smemory<char> mo2; //将Smemory实例化，并创建对象mo2
    for(i=0; i<8;i++)
    {
       mo1.mput(i);//调用成员函数mput()
       mo2.mput(ch); ch++; //调用成员函数mput()
    }
    cout<<"Get mo1 => ";
    for(i=0;i<8;i++)
       cout<<mo1.mget( );//调用成员函数mget()
    cout<<"\nGet mo2 => ";
    for(i=0;i<8;i++)
       cout<<mo2.mget( ); //调用成员函数mget()
	cout<<endl;
    
    
    //========
	//LoadOperInfo()新建一个类对象,适用于传参数的情况
    foreach_OperInfo(LoadOperInfo()); //一个类来处理一个结构，而不是一个函数
    foreach_OperInfo(process);//用一个函数来处理结构
}

