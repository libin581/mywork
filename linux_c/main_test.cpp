/* C++�����ǲ������еĶ������� main( )���������  
���ǡ�����C++������ԣ���̬������ȫ�ֱ�����ȫ�ֶ���ķ������� main( )����֮ǰ����
������ˡ����ԣ����������еĶ��������� main( )����ģ�main( )ֻ������һ��Լ���ĺ���
��ڣ���main( )�����еĴ���ִ��֮ǰ�������һ���ɱ��������ɵ�_main( )��������_main( )
�������������ȫ�ֶ���Ĺ��켰��ʼ�������� */

#include<iostream> 
using namespace std; 

class A 
{ 
     public: 
         A() {cout<<"construct"<<endl;} 
         ~A() {cout<<"destruct"<<endl;} 
}; 
 
A a; 
int main( ) 
{ 
     cout<<"main"<<endl; 
     return 0; 
}

