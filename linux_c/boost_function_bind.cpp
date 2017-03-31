//����ģ��������ַ������ͣ����������������������Ͳ�ͬ�ĸ��ֺ���
//typedef boost::function<void()> Func;
//or
//typedef boost::function<void(void)> Func;
//ע��Funcû�з���ֵ�����ܻ�ȡʵ�������ķ���ֵ
//Ҳ���ܴ������


#include<boost/function.hpp>
#include<boost/bind.hpp>
#include<iostream>

typedef boost::function<void(void)> Func;

int test(int num)
{
   std::cout<<"In test:"<<num<<std::endl;    
}

int cpp(int *ptr)
{
    std::cout<<"In CPP"<<std::endl;    
    return 10;
}

int main()
{
  Func f;
  f=boost::bind(test,6);
  f(); //f(6)
  
  f.clear();
  
  int *ptr = NULL;
  f=boost::bind(cpp,ptr);
  f();
}